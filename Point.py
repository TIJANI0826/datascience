from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Point({}, {})".format(self.x,self.y)

    def __add__(self,other):
        x_ad = self.x + other.x
        y_ad = self.y + other.y
        return Point(x_ad,y_ad)
    
    def __sub__(self,other):
        x_sub = self.x - other.x
        y_sub = self.y - other.y
        return Point(x_sub,y_sub)
        
    def __mul__(self,other):
        if type(other) == int:
            return Point(self.x * other,self.y * other)
        return other.x * self.x + other.y * self.y 

    def distance(self, other):
        return sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))
    
    def __repr__(self):
        return 'Point({},{})'.format(self.x, self.y)
c = Point(1,2)
print(c.x)