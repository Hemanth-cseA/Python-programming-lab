#reverse of a string
def reverse(str): 
  s = "" 
  for i in str: 
    s = i + s
  return s
print("enter the string")
str=input()
print(reverse(str))