#regular expressions
import re
pattern=r"[\w.-]+@[\w.-]+"
string="Please send your fedback at info@oxford.com"
match=re.search(pattern,string)
if match:
    print("Email to:",match.group())
else:
    print("no match")
pattern=r"^[0-9]+ .*"
string="12 abc"
match=re.search(pattern,string)
if match:
    print("match")
result=re.findall(r'.',"good going")
print(result)
result1=re.findall(r'\w+',"good going")
print(result1)
result2=re.findall(r'\w+$',"good going")
print(result2)
result3=re.findall(r'\w\w\w',"good going")
print(result3)