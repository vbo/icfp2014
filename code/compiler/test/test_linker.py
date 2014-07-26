import unittest

from .. compile import CompilationUnit
from .. compile import Linker


class SourceLoader(object):

    def __init__(self, sources):
        self.sources = {}
        for k, v in sources.iteritems():
            self.sources[k] = CompilationUnit(k, v)

    def __call__(self, prefix, name):
        try:
            return self.sources[name]
        except KeyError:
            raise IOError("No such file: <test>/" + name)


class LinkerTestCase(unittest.TestCase):

    def test_single(self):
        sources = {
            "main": """
                LD 0 0
            """
        }
        ld = SourceLoader(sources)
        l = Linker(ld)
        code = l.link(ld("programs", "main"))
        self.assertEqual(code, "LD 0 0")

        sources = {
            "main": """
                LDF @zero
                RTN
            """,
            "zero": """
                LDC 0
                RTN
                LDF @recursive
            """,
            "recursive": """
                LDC 1
                ATOM
                LDF @recursive
                LDF @zero
            """
        }
        ld = SourceLoader(sources)
        l = Linker(ld)
        code = l.link(ld("programs", "main"))
        self.assertEqual(code, "\n".join([
            "LDF 2",
            "RTN",
            "LDC 0",
            "RTN",
            "LDF 5",
            "LDC 1",
            "ATOM",
            "LDF 5",
            "LDF 2"
        ]))

        sources = {
            "main": """
                LDC %one
                LDC 4
                ; bla bla
                ; hello world!
                LDF @add
                AP 2


                LDC 0
                LDC 24
                LDC 4
                LDF @add_or_sub
                AP 3
                RTN
            """,
            "add": """
                ; add two digits from args
                LD 0 0
                LD 0 1
                ADD
                RTN
            """,
            "add_or_sub": """
                LD 0 0
                TSEL $sub $add
                $sub:
                LD 0 1
                LD 0 2
                SUB
                RTN

                $add:
                LD 0 1
                LD 0 2
                ADD
                RTN
            """
        }
        ld = SourceLoader(sources)
        l = Linker(ld)
        code = l.link(ld("programs", "main"))
        self.assertEqual(code, "\n".join([
            "LDC 1",
            "LDC 4",
            "LDF 10",
            "AP 2",
            "LDC 0",
            "LDC 24",
            "LDC 4",
            "LDF 14",
            "AP 3",
            "RTN",
            "LD 0 0",
            "LD 0 1",
            "ADD",
            "RTN",
            "LD 0 0",
            "TSEL 16 20",
            "LD 0 1",
            "LD 0 2",
            "SUB",
            "RTN",
            "LD 0 1",
            "LD 0 2",
            "ADD",
            "RTN"
        ]))
