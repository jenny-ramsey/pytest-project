
class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)

    def output(self):
        return self.str

string = StringBuilder()
string.add("Hello, ")
string.add("world!")
print(string.size())
print(string.output())