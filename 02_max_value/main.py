class maxvalue:
    def __init__(self, lst):
        self.lst = lst
        self.max_value = float('-inf')

    def find_max_value(self):
        for i in self.lst:
            if i > self.max_value:
                self.max_value = i

        return self.max_value


if __name__ == '__main__':
    output = maxvalue([3, 8, 5, 7, 4])
    print(output.find_max_value())