#regular expression plural
import re
def pluralize(noun):
    if re.search('[six]$',noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiousgkprt]h$',noun):
        return re.sub('$','es',noun)
    elif re.search('[aeiou]y$',noun):
        return re.sub('y$','ies',noun)
    else:
        return noun + 's'
list=["bush","fox","toy","cap"]
for i in list:
    print(i,'-',pluralize(i))