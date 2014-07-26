def replace_function_names(lines, functions):
    result = []
    for line in lines:
        if line.startswith('LDF'):
            literals = line.split(' ')
            line = 'LDF ' + str(functions[literals[1]]) #+ '    ; call something, probably ' + unit.name  as no unit name here
        result += [line]
    return result


def get_marks(lines):
    marks = {}
    for i, line in enumerate(lines):
        c = line.find(';')
        if c >= 0:
            marks[line[c + 1:].strip()] = i
    return marks


def replace_marks(lines, marks, line_no):
    result = []
    for line in lines:
        code = line
        comment = ''
        if line.find(';') >= 0:
            (code, comment) = line.split(';')
        for mark in marks:
            place = code.find(mark)
            if place >= 0:
                code = code[:place] + str(int(marks[mark]) + line_no) + code[place + len(mark):]
        new_line = code
        if len(comment):
            new_line += ';' + comment
        result += [new_line]
    return result


def replace_common(lines, line_no):
    marks = get_marks(lines)
    result = replace_marks(lines, marks, line_no)
    return result


class CompilationUnit(object):
    def __init__(self, name, lines=None):
        self.name = name
        self.lines = []
        if lines:
            for line in lines.split("\n"):
                line = line.strip()
                if not line:
                    continue
                self.lines.append(line)
        self.instructions_count = len(self.lines)

    def load_source(self, prefix):
        for line in file(prefix + '/' + self.name + '.gcc'):
            line = line.strip()
            if not line:
                continue
            self.instructions_count += 1
            self.lines.append(line)

    def compile(self, line_no):
        return replace_common(self.lines, line_no)


class Function(CompilationUnit):
    def __init__(self, name, lines=None):
        super(Function, self).__init__(name, lines)
        if not lines:
            self.load_source("functions")


class Program(CompilationUnit):
    def __init__(self, name, lines=None):
        super(Program, self).__init__(name, lines)
        if not lines:
            self.load_source("programs")


#compilation_units = [Program('test'), Function('LOAD_DATA1')]
compilation_units = [Program('TEST_TUPLE_AT'), Function('TEST_LOAD_TUPLE'), Function('TUPLE_AT')]
#compilation_units = [Program('main'), Function('STEP'), Function('MAP_AT'), Function('LIST_VAL_AT'),
                    #Function('GET_NEXT_DIRECTION'), Function('POINTS_EQ'), Function("GET_VALUABLE_NEIGHBOR"),
                    #Function('IS_VALUABLE'), Function('DIR_FROM_TO'), Function('DIR_TO_VALUABLE_NEIGHBOR')]
                    #Function('TEST_GET_VALUABLE_NEIGHBOR'), Function('LIST_VAL_AT'), Function('LOAD_DATA1')]
#compilation_units = [Program('main'), Function('STEP'), Function('MAP_AT'), Function('LIST_VAL_AT'),
                    #Function('GET_NEXT_DIRECTION'), Function('POINTS_EQ')]

#compilation_units = [
#        Program(
#            'test',
#            """
#                LDF TEST_LOAD_GHOSTS
#                AP 0
#                LDC 8
#                LDC 10
#                CONS
#                BRK
#                LDF IS_DANGER
#                AP 2
#                STOP
#            """
#        ),
#        Function(
#            'TEST_LOAD_GHOSTS'
#        ),
#        Function(
#            'FOREACH'
#        ),
#        Function(
#            'FOREACH3'
#        ),
#        Function(
#            'ABS_SUB'
#        ),
#        Function(
#            'IS_CLOSE'
#        ),
#        Function(
#            'IS_DANGER'
#        ),
#        Function(
#            'IS_DANGER_ONE_GHOST'
#        ),
#]

if __name__ == '__main__':
    instruction_no = 0
    code = []
    functions = {}
    for unit in compilation_units:
        code += unit.compile(instruction_no)
        if type(unit) is Function:
            functions[unit.name] = instruction_no
            code[instruction_no] += '    ; def ' + unit.name
        instruction_no += unit.instructions_count
    code = replace_function_names(code, functions)
    code += " "
    print "\n".join(code)

