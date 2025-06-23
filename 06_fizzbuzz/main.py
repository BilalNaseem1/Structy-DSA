def fizz_buzz(n):
  x = []
  for i in range(1, n+1):
    if i%3==0 and i%5 == 0:
      i = "fizzbuzz"
      x.append(i)
    elif i%3 ==0:
      i = "fizz"
      x.append(i)
    elif i%5==0:
      i = "buzz"
      x.append(i)
    else:
      x.append(i)
    
  return x


if __name__ == "__main__":
  print(fizz_buzz(20))