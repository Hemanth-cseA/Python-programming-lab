num =[]
for i in range(1,10):
    num = [x for x in num if x%2!=0]
    num.append(i)
print(num)