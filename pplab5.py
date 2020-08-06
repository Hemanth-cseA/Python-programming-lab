#armstrong number or not
num=int(input("enter number\n"))
n=num
arm=0
while(num>0):
  a=num%10
  arm=arm+(a**3)
  num=num//10
if n==arm:
  print(n,"is a Armstrong number")
else:
  print(n,"is not a Armstrong number")