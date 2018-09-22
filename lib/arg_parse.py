import argparse

class ArgParser():
    def __init__(self):
        # Initialization of the parser of arguments
        self.argparser = argparse.ArgumentParser(description="Appends text to a file")
        self.argparser.add_argument('file', metavar='f', type=str, help="Path to the file to append")
        self.arguments = None

    def get_args(self):
        if not self.arguments:
            self.arguments = self.argparser.parse_args()
        return self.arguments

    def get_arg(self, name):
        if not self.arguments:
            self.arguments = self.argparser.parse_args()
        return self.arguments[name]
        
