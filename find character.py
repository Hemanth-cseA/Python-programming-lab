#find character
print("enter the string")
str=input()
print("enter the character to be searched:")
x=input()
for i in range(0,len(str)):
        if(x==str[i]):
            print("character ", x," is present at index",i)
        else:
          print("not found")