def replace_lines(line, line_no):
    line_result = []
    literals = line.split(' ')
    for literal in literals:
        if literal.isdigit():
            literal = str(int(literal) + line_no - 1)
        line_result.append(literal)
    line = ' '.join(line_result)
    return line

def replace_lines_starts_with(lines, starts, line_no):
    for start in starts:
        result = []
        for line in lines:
            if line.startswith(start):
                line = replace_lines(line, line_no)
            result += [line]
        lines = result
    return lines

class Function(object):
    def __init__(self, name):
        self.name = name
        self.lines = []
        for line in file('functions/' + name + '.gcc'):
            self.lines.append(line.strip())

    def compile(self, line_no):
        return replace_lines_starts_with(self.lines, ['SEL'], line_no)

class Program(object):
    def __init__(self, name):
        self.name = name
        self.lines = []
        for line in file('programs/' + name + '.gcc'):
            self.lines.append(line.strip())

    def compile(self, line_no):
        return self.lines


def replace_function_names(lines, functions):
    result = []
    for line in lines:
        if line.startswith('LDF'):
            literals = line.split(' ')
            line = 'LDF ' + str(functions[literals[1]]) + '    ; call ' + instruction.name
        result += [line]
    return result

instructions = [ Program('MAIN'), Function('ADD_OR_SUB') ]

if __name__ == '__main__':
    line_no = 0
    code = []
    functions = {}
    for instruction in instructions:
        code += instruction.compile(line_no)
        if type(instruction) is Function:
            functions[instruction.name] = line_no
            code[line_no] += '    ; def ' + instruction.name
        line_no = len(code)
    code = replace_function_names(code, functions)
    print "\n".join(code)

