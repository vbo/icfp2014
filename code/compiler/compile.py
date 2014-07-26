import sys
import os.path
import re

from . import gcc

# %something macro
# $something: define label, $something - use label
# @something call external func


# use %something to access macro
macros = {
    # some may be used in test, don't remove
    "MACROS_WORK?": """
        ; do something
        LD 0 0
    """,
    "up": "0",
    "right": "1",
    "down": "2",
    "left": "3",

    "wall": "0",
    "empty": "1",
    "pill": "2",
    "power_pill": "3",
    "fruit": "4",
    "lambda_start": "5",
    "ghost_start": "6",
    "inc": """
        LDC 1
        ADD
    """,
    "dec": """
        LDC 1
        SUB
    """
}

class Error(Exception):
    pass


class CompilationUnit(object):

    ALLOW_NO_RTN = False
    EOI_RE = r"(?:$|;.*)"

    def __init__(self, name, source):
        # pre-cleanup, macro-replace, local jumps
        self.name = name
        self.labels = {}
        self.dep_funcs = set()
        self.instructions_count = 0
        for k, v in macros.iteritems():
            source = source.replace("#" + k, v)
        self.lines = []
        expect_line = False
        has_rtn = False
        for line in source.split("\n"):
            line = line.strip()
            if not line or line.startswith(';'):
                continue
            label_match = re.match(r'\$(\w+):' + self.EOI_RE, line)
            if label_match:
                label_name = label_match.groups()[0]
                if label_name in self.labels:
                    raise Error("Duplicate label %s - redefined (line_no: %s, unit: %s)" % (
                        label_name, self.instructions_count, self.name))
                self.labels[label_name] = self.instructions_count
                expect_line = True
                continue
            dep_call_match = re.search(r'@(\w+)', line)
            if dep_call_match:
                dep_name = dep_call_match.groups()[0]
                self.dep_funcs.add(dep_name)
                # do not exec continue - it's just a normal line
            instr_match = re.match(r'(\w+).*', line)
            if not instr_match:
                raise Error("Bad line: |%s| (line_no: %s, unit: %s)" % (line, self.instructions_count, self.name))
            instr = instr_match.groups()[0]
            if instr not in gcc.instructions:
                raise Error("No such instruction: |%s| (line: %s, line_no: %s, unit: %s)" % (instr, line, self.instructions_count, self.name))
            if instr == "RTN":
                has_rtn = True
            expect_line = False
            self.lines.append(line)
            self.instructions_count += 1
        if expect_line:
            raise Error("Expected line after '%s'" % (self.lines[-1]))
        if not self.ALLOW_NO_RTN and not has_rtn:
            raise Error("RTN required at unit: %s" % (self.name,))

    def generate_code(self, code_ref, dep_refs):
        code = "\n".join(self.lines)
        for lab, ref in self.labels.iteritems():
            code = code.replace("$" + lab, str(code_ref + ref))
        for dep in self.dep_funcs:
            code = re.sub(r"@" + dep + r"\b", str(dep_refs[dep]), code)
        return code

    def load_source(self, prefix):
        for line in file(prefix + '/' + self.name + '.gcc'):
            line = line.strip()
            if not line:
                continue
            self.instructions_count += 1
            self.lines.append(line)


class Linker(object):

    def __init__(self, source_loader):
        self.source_loader = source_loader
        self.units = {}
        self.units_in_order = []
        self.code_pos = 0

    def link(self, unit):
        self._link_all(unit)
        code = []
        for u in self.units_in_order:
            dep_refs = {}
            for dep in u.dep_funcs:
                dep_refs[dep] = self.units[dep].start
            code.append(u.generate_code(u.start, dep_refs))
        return "\n".join(code)

    def _link_all(self, unit):
        if unit.name in self.units:
            raise Error("%s unit compiled more then once" % (unit.name,))
        self.units[unit.name] = unit
        self.units_in_order.append(unit)
        unit.start = self.code_pos
        self.code_pos += unit.instructions_count
        for d in unit.dep_funcs:
            if d in self.units:
                continue
            self._link_all(self.source_loader("functions", d))


if __name__ == '__main__':
    def unit_from_file(prefix, name):
        return CompilationUnit(name, file(unit_from_file.source_root + "/" + prefix + "/" + name + ".gcc").read())

    if len(sys.argv) < 2:
        print "Usage: %s <progname>" % sys.argv[0]
        exit()

    script = os.path.realpath(sys.argv[0])
    root = os.path.dirname(script)
    unit_from_file.source_root = root
    comp = Linker(unit_from_file)
    code = comp.link(unit_from_file("programs", sys.argv[1]))
    print code

