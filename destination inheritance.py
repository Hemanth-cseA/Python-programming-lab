class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return (self.x,self.y)
class location:
    def __init__(self,x1,y1,x2,y2):
        self.source=point(x1,y1)
        self.destination=point(x2,y2)
    def show(self):
        print("source=",self.source.get())
        print("destination=",self.destination.get())
    def reflection(self):
        self.destination.x=-self.destination.x
        print("reflection point on x axis is:",self.destination.x,self.destination.y)
L=location(1,2,3,4)
L.show()
L.reflection()
