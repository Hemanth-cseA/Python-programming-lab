#prime number or not
num=int(input("enter number\n"))
if num>1:
  for i in range(2,num):
    if num%i==0:
      print(num,"is not a prime number\n")
      print(i,"times",num//i,"is",num)
  else:
    print(num,"is a prime number")
else:
  print(num,"is not a prime number")