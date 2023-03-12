class Printer:
    def __init__(self, char, width, height):
        self.char = char
        self.width = width
        self.height = height

    def set_char(self, x):
        self.char = x

    def print(self):
        for i in range(self.height):
            print(self.char * self.width)

myPrinter = Printer('0', 6, 2)
myPrinter.print()
myPrinter.set_char('.')
myPrinter.print()