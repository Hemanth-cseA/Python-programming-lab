#occurence of a character
print("ente the string")
str=input()
print("enter the character to be searched:")
x=input()
count=0
for i in range(0,len(str)):
        if(x==str[i]):
            count=count+1
print(x,"occurred ",count,"times")
        