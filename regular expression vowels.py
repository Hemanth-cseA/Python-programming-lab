#regular expression vowels
import re
pattern=r'[aeiou]'
if re.search(pattern,"bcdfg"):
    print("match found")
else:
    print("not found")