#multuplication table using function
num=int(input("enter number\n"))
def table(num):
   for i in range(1,11):
     print(num,"x",i,"=",num*i,"\n")
table(num)