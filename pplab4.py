#palindrome of string
s=input("enter the string\n")
for i in range(0,int(len(s)/2)):
  if s[i]!=s[len(s)-i-1]:
    print(s,"is not a palindrome\n")
  else:
    print(s,"is a palindrome\n")
