#fibonacci series
def fibonacci(num):
  if n==0 or n==1:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)
num=int(input("enter the number"))
if num<=0:
  print("enter a positive integer")
else:
  print("fibonacci serues of",fibonacci(num))