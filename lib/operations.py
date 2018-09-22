import sys
import readline

class Operations():
    def __init__(self, file_pointer, line_number=1):
        self.file_lines = file_pointer.readlines()
        self.line_number = len(self.file_lines)-1
        self.current_operator = None

    def change_line(self, line_number):
        if line_number < 0 or line_number > len(self.file_lines):
            print("WARN: Line number exceeds file lines", file=sys.stderr)
            return False
        else:
            self.line_number = line_number
            return True

    def print(self):
        for line in self.file_lines:
            sys.stdout.write(line)

    def enumerate(self):
        for (index, line) in enumerate(self.file_lines):
            if self.line_number == index:
                sys.stdout.write(str(index) + " ->\t" + line)
            else:
                sys.stdout.write(str(index) + "\t" + line)

    def append(self, line_number=None, changed_line=None):
        import pdb; pdb.set_trace()
        if line_number == None:
            line_number = self.line_number
        exit_condition = False
        appended_lines = []
        self.current_operator = 'a'
        if changed_line:
            def insert_changed_line():
                readline.insert_text(changed_line)
                readline.redisplay()
            readline.set_pre_input_hook(insert_changed_line)
        while(not exit_condition):
            new_line = input()
            readline.set_pre_input_hook()
            if new_line == ".":
                exit_condition = True
            else:
                appended_lines.append(new_line + '\n')
        if line_number < len(self.file_lines):
            existing_lines = self.file_lines[line_number+1:]
            appended_lines = appended_lines + existing_lines
        self.file_lines = self.file_lines[0:line_number+1] + appended_lines
        self.line_number = self.line_number + len(appended_lines)

    def insert(self):
        return self.append(self.line_number-1)

    def delete(self, line_number=None):
        delete_line = line_number
        if delete_line == None:
            delete_line = self.line_number
        self.file_lines = [line for (index, line) in enumerate(self.file_lines) if index != delete_line]

    def change(self, line_number=None):
        change_line = line_number
        if change_line == None:
            change_line = self.line_number
        old_line = self.file_lines[change_line]
        # Change(line) = delete(line) + append(line-1)
        self.delete(change_line)
        self.append(change_line-1, old_line.rstrip())

    def move(self, to_line, from_line=None):
        line = from_line
        if line == None:
            line = self.line_number
        self.file_lines.insert(to_line+1, self.file_lines[line])
        if from_line == None:
            self.delete(from_line)
