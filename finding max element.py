#3. Write a program that has a class numbers with values stored in a list. Write a class method to find the largest value.
class numbers:
    def __init__(self):
        self.values = []
    def find_max(self):
        max = ''
        for i in self.values:
            if(i > max):
                max=i
        print('Maximum element: %r' %max)
    def insert_element(self):
        value = input('Enter value: ')
        self.values.append(value)
x = numbers()
ch = 'y'
while(ch == 'y'):
    x.insert_element()
    ch = input('Do you wish to enter more elements?')
x.find_max()
