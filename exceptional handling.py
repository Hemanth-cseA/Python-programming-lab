try:
    num=int(input("Enter the number: "))
    print(num**2)
except(KeyboardInterrupt):
    print("You should have entered a number..program terminating.")
except(ValueError):
    print("Please check before you enter..program terminating")
print("Bye")


try:
    num=int(input("Enter the number: "))
    print(num**2)
except(KeyboardInterrupt,ValueError,TypeError):
    print("Please check before you enter..program terminating")
print("Bye")