
class heyProgrammer:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "hey "+self.name
    

if __name__ == "__main__":
    programmer = heyProgrammer("Bilal")
    print(programmer.greet())