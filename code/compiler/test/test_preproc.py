import unittest

from .. compile import CompilationUnit
from .. compile import Error

CompilationUnit.ALLOW_NO_RTN = True
CompilationUnit.PRINT_UNIT_NAME = False
CompilationUnit.PRINT_INSTR_CNT_DBUG = False


class PreprocTestCase(unittest.TestCase):

    def test_all(self):
        u = CompilationUnit("comments", """
            ; hello world
        """)
        self.assertEqual(u.instructions_count, 0)
        self.assertEqual(u.lines, [])

        u = CompilationUnit("comments", """
            ; hello world
            LD 0 0
        """)
        self.assertEqual(u.instructions_count, 1)
        self.assertEqual(u.lines, ["LD 0 0"])

    def test_macro(self):
        u = CompilationUnit("macro", """
            #MACROS_WORK
            ; or not?
        """)
        self.assertEqual(u.instructions_count, 3)
        self.assertEqual(u.lines, ["ADD", "SUB", "LD 0 0"])

        u = CompilationUnit("macro_local", """
            !def local_macro LD 0 2
            #local_macro
            ; or not?
        """)
        self.assertEqual(u.instructions_count, 1)
        self.assertEqual(u.lines, ["LD 0 2"])

        u = CompilationUnit("macro", """
            !def loc ADD, ADD
            #loc
        """)
        self.assertEqual(u.instructions_count, 2)
        self.assertEqual(u.lines, ["ADD", "ADD"])

    def test_labels(self):
        u = CompilationUnit("macro", """
            $lab1:
                LD 0 0
        """)
        self.assertEqual(u.instructions_count, 1)
        self.assertEqual(u.lines, ["LD 0 0"])
        self.assertEqual(u.labels, {'lab1': 0})

        try:
            u = CompilationUnit("expected_line", """
                LD 0 0
                $lab1:
            """)
            self.fail("Exception expected")
        except Error as e:
            pass

        try:
            u = CompilationUnit("redefine_label", """
                LD 0 0
                $lab1:
                    LDC 0
                $lab1:
                    LDC 1
            """)
            self.fail("Exception expected")
        except Error as e:
            pass

    def test_deps(self):
        u = CompilationUnit("deps", """
            LDF @extern
        """)
        self.assertEqual(u.instructions_count, 1)
        self.assertEqual(u.dep_funcs, set(("extern",)))
