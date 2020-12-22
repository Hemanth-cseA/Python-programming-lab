Dict = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def chk_leapyear(year):
    if(year%4==0 and year%100 !=0) or (year%400==0):
        return 1
    else:
        return 0
class Date:
    def __init__(self):
        d = m = y = 0
    def get(self):
        self.d = int(input("enter the day : "))
        self.m = int(input("enter the month : "))
        self.y = int(input("enter the year : "))
    def __add__(self, num):
        self.d += num
        if self.m != 2:
            max_days = Dict[self.m]
        elif self.m == 2:
            isleap = chk_leapyear(self.y)
            if isleap == 1:
                max_days = 29
            else:
                max_days = 28
        while self.d > max_days:
            self.d -= max_days
            self.m += 1
        while self.m > 12:
            self.m -= 12
            self.y += 1
    def display(self):
        print(self.d, "-" , self.m, "-" , self.y)
D = Date()
D.get()
num = int(input("how many days to add : "))
D + num
D.display()
