#regular expressions telephone
import re
list=['7838456789','1234567890','7894561231','9618242748']
for i in list:
    result=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if result:
        print(result,end=" ")