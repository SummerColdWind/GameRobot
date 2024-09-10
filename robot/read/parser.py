import re

END_SYMBOL = 'end'
SPECIAL_TYPES = ('if', 'while', 'for', 'else', END_SYMBOL, 'exec')
VAR_PATTERN = re.compile(r'\$(\w+)')
SPACE_PATTERN = re.compile(r'(\S+=".*?"|\S+)')


class Parser:
    def __init__(self):
        self.vars = {}
        self.stack = []
        self.statements = []
        self.pointer = self.statements
        self.lines = ''
        self.exec = False
        self.indent = -1


    def __call__(self, path):
        self.__init__()
        self.load(path)
        self.parse()
        return self.statements

    def load(self, path):
        if isinstance(path, str):
            with open(path, 'r', encoding='utf-8') as file:
                self.lines = file.readlines()
        else:
            self.lines = path

    def parse(self):
        print('=' * 20)
        print('Parsing start: ')
        for line in self.lines:
            print(line.rstrip('\n'), end='')
            # Native statement
            if self.exec and line.strip() != END_SYMBOL:
                if self.indent < 0:
                    self.indent = len(line) - len(line.lstrip())
                    self.pointer.append(line.lstrip())
                else:
                    indent = len(line) - len(line.lstrip()) - self.indent
                    self.pointer.append(' ' * indent + line.lstrip())
                continue

            line = line.strip()

            # Comment statement or empty
            if line.startswith('#') or not line:
                continue

            try:
                symbol, rest = line.strip().split(' ', 1)
            except ValueError:
                symbol, rest = line.strip(), ''

            # Command statement
            if symbol not in SPECIAL_TYPES:
                statement = {'type': symbol}
                matches = SPACE_PATTERN.finditer(rest)
                params = [match.group(0) for match in matches]
                for param in params:
                    key, value = (x.strip() for x in param.split('=', 1))
                    try:
                        statement[key] = eval(value)
                    except (SyntaxError, NameError):
                        statement[key] = value

            # Logical statement
            elif symbol == 'exec':
                # single line
                if rest:
                    statement = {'type': 'exec', 'then': [rest]}
                # multiline
                else:
                    then = []
                    statement = {'type': 'exec', 'then': then}
                    self.stack.append(statement)
                    self.pointer = then
                    self.exec = True
                    continue
            elif symbol == 'if':
                _, condition = (x.strip() for x in line.strip().split(' ', 1))
                then, els = [], []
                statement = {'type': 'if', 'condition': condition, 'then': then, 'else': els}
                self.stack.append(statement)
                self.pointer = then
                continue
            elif symbol == 'else':
                self.pointer = self.stack[-1]['else']
                continue
            # while statement
            elif symbol == 'while':
                _, name = (x.strip() for x in line.strip().split(' ', 1))
                then = []
                statement = {'type': 'while', 'name': name, 'then': then}
                self.stack.append(statement)
                self.pointer = then
                continue
            # for statement
            elif symbol == 'for':
                _, times = (x.strip() for x in line.strip().split(' ', 1))
                then = []
                statement = {'type': 'for', 'times': int(times), 'then': then}
                self.stack.append(statement)
                self.pointer = then
                continue
            # end
            elif symbol == END_SYMBOL:
                if self.exec:
                    self.exec = False
                    self.indent = -1
                statement = self.stack.pop()
                if self.stack:
                    self.pointer = self.stack[-1]['then']
                else:
                    self.pointer = self.statements
            else:
                raise SyntaxError

            self.pointer.append(statement)
        print('Parsing successful end.')
        print('=' * 20)
