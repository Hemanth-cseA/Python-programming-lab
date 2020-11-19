#dictorines
dict={'roll_no':'19h61a0518','name':'saikiran','course':'B.Tech'}
print(dict)
dict1={x:2^x for x in range(1,10)}
print(dict1)
print(dict['roll_no'])
print(dict['name'])
print(dict['course'])
dict['marks']=95
print(dict)
dict['course']='bcom'
print(dict)
del dict['marks']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)