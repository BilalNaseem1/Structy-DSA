

def pairProduct(lst):
    print("---- enumerate -----")
    for i in enumerate(lst):
        print(i)

    print("without enumerate")
    for i in lst:
        print(i)




if __name__ == "__main__":
    print(pairProduct([1, 9, 4, 7, 2, 3]))