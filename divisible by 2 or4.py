#list 1-20 divisible by 2 and 4
div=[]
for i in range(1,20):
    if(i%2==0 or i%4==0):
        div.append(i)
print(div)