#factorial if a number
def factorial(num): 
  if num==0:
    return 1
  else:
    return(num*factorial(num-1))
n=int(input("enter the number"))
if n==0:
  print("the factorial of 0 is 1")
else:
  print("the factorial of",n,"is",factorial(n))