def replace_function_names(lines, functions):
    result = []
    for line in lines:
        if line.startswith('LDF'):
            literals = line.split(' ')
            line = 'LDF ' + str(functions[literals[1]]) + '    ; call ' + instruction.name
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
                print code, place, marks[mark], line_no
                code = code[:place] + str(int(marks[mark]) + line_no) + code[place + len(mark):]
        new_line = code
        if len(comment):
            new_line += ';' + comment
        result += [new_line]
    return result

def replace_common(lines, line_no):
    marks = get_marks(lines)
    print marks
    result = replace_marks(lines, marks, line_no)
    return result

class Function(object):
    def __init__(self, name):
        self.name = name
        self.lines = []
        for line in file('functions/' + name + '.gcc'):
            self.lines.append(line.strip())

    def compile(self, line_no):
        return replace_common(self.lines, line_no)

class Program(object):
    def __init__(self, name):
        self.name = name
        self.lines = []
        for line in file('programs/' + name + '.gcc'):
            self.lines.append(line.strip())

    def compile(self, line_no):
        return replace_common(self.lines, line_no)

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

