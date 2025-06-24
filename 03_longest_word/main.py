class longestword:
    def __init__(self, sentence):
        self.sentence = sentence
        self.longest_word_length = float('-inf')

    def findlongest(self):
        self.lst = self.sentence.split()
        self.longest_word = self.lst[0]

        for i in self.lst:
            if len(i) > self.longest_word_length:
                self.longest_word = i
                self.longest_word_length = len(i)

        return self.longest_word
    
if __name__ == '__main__':
    output = longestword("what a wonderful world")
    result = output.findlongest()
    print(result)