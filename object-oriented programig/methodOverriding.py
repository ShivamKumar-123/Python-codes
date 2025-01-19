import math
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        # return round((math.pi * self.radius**2),)
        return round((math.pi * super().area()),2)


rec = Shape(3,5) 
print(rec.area())

c = Circle(5)
print(c.area())
