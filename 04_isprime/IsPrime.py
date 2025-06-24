import math

class IsPrime:
    def __init__(self, n):
        self.n = n
        self.x = int(math.sqrt(n))


    def findisprime(self):
        if self.n <=1:
            return False
        
        for i in range(2, self.x+1):
            if self.n%i == 0:
                return False
            
        return True
        


if __name__ == "__main__":
    result = IsPrime(100)
    output = result.findisprime()
    print(output)