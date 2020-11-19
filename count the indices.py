list1=[1,2,2,3,4,5,4,4,5,6,7]
print("enter the no.")
x=int(input())
c=0
ind=0
print("index values:")
for i in list1:
    if x==i:
        print(ind)
        c+=1
    ind+=1
print("count :",c)