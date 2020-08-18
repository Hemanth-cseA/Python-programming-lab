#squares of number from 1 to 100 end with 4 or 9
for i in range(1,100):
  a=i*i
  b=a%10
  if(b==4):
    print(i,"it's square end with 4")
  if(b==9):
    print(i,"it's square end with 9")