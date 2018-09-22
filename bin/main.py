import sys
import re

from context import ArgParser
from context import Operations

LINE_NUMBER_PATTERN = re.compile('^[0-9]{1,}(?!$)')

def main():
    argparser = ArgParser()
    args = argparser.get_args()
    command_history = []
    # The only argument available will be the file to open and append
    if args.file:
        try:
            file = open(args.file, 'r')
            operations = Operations(file, 0)
            file.close()
        except OSError as os_error:
            print("ERROR: File can't be opened", file=sys.stderr)
            exit()
        while True:
            input_line = input(' > ')
            regex_line_number = LINE_NUMBER_PATTERN.search(input_line)
            if regex_line_number:
                result = operations.change_line(int(regex_line_number.group(0)))
                operation = input_line[regex_line_number.end():]
                if not result:
                    # Skip current operation, as it contains errors
                    continue
            else:
                operation = input_line
            if operation == 'q':
                break
            elif operation == 'a':
                operations.append()
            elif operation == 'p':
                operations.print()
            elif operation == 'n':
                operations.enumerate()
            elif operation == 'i':
                operations.insert()
            elif operation == 'd':
                operations.delete()
            elif operation == 'c':
                operations.change()
            elif operation[0] == 'm':
                regex_to_line = re.compile("[0-9]+$").search(operation)
                if regex_to_line:
                    operations.move(int(regex_to_line.group(0)))
                else:
                     print("WARN: Move operation needs the new address of the line", file=sys.stderr)
            elif operation.isdigit():
                operations.change_line(int(operation))
            else:
                print("WARN: Operation not understood", file=sys.stderr)
        try:
            file_write = open(args.file, 'w')
            file_write.write(''.join(operations.file_lines))
            file_write.close()
        except OSError as os_error:
            print("ERROR: File can't be written. Changes were lost!", file=sys.stderr)
            exit()
    

if __name__ == "__main__":
    main()
