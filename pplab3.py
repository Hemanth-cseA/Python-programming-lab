#a number palindrome or not
num=int(input("enter number\n"))
a=num
rev=0
while(num!=0):
  n=num%10
  rev=(rev*10)+n
  num=num//10
if(rev==a):
  print(a,"is a palindrome")
else:
  print(a,"is not a palindrome")