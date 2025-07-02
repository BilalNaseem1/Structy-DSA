
def aPairs(lst_):
    final_list = []

    x=0
    for i in range(x, len(lst_)):
        for j in range(x+1, len(lst_)):

            final_list.append([lst_[i], lst_[j]])
        x+=1 
            
    return final_list



if __name__ == "__main__":
    output = aPairs(["a", "b", "c"])
    print(output)
