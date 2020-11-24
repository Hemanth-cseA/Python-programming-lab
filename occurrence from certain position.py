#occurence from specified position
def search(str,x,n):
    count=0
    i=n
    for i in range(0,len(str)):
        if(x==str[i]):
            count+=1
    print("This character occured ",count," times")
print("\nEnter the string")
str=input()
print("Enter the character to be searched:")
x=input()
print("enter the position")
n=input()
search(str,x,n)