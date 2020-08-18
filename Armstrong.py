#armstrong number in given range
a=int(input("enter the least number the range"))
b=int(input("enter the greatest number of the range"))
for i in range(a,b+1):
  sum=0
  temp=i
  while(temp>0):
    digit=temp%10
    sum+=temp**3
    temp//=10
  if(sum==i):
    print(i,"is a Armstrong number")