class counter:
    def __init__(self, string):
        self.string = string
        self.counter_dict = {}

    def generate_counter(self):
        
        for i in self.string:
            if i not in self.counter_dict:
                self.counter_dict[i] = 0
            
            self.counter_dict[i] +=1

        return self.counter_dict
    

if __name__ == "__main__":
    cls = counter("amazing")
    output = cls.generate_counter()

    print(output)
        