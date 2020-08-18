#sum of digits
def sum_of_digits(number):
  global sum
  if(number>0):
    reminder=number%10
    sum = sum + reminder
    sum_of_digits(number//10)
  return sum
n=int(input("enter the number"))
s=sum_of_digits(n)
print(n)