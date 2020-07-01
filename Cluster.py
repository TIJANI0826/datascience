from Point import Point
class Cluster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.center = Point(x, y)
        self.points = [Point(self.x,self.y)]
    def __repr__(self):
        return "points are: {}".format(self.points)

    def update(self):
        """ find the avrage of the points and make it the centroid"""
        ad = [point for point in self.points]
        l_x = []
        l_y = []
        for a in ad:
            l_x.append(a.x)
            l_y.append(a.y)
        self.center = Point( sum(l_x)//len(l_x), sum(l_y)//len(l_y) )
    
    def add_point(self, point):
        return self.points.append(point)

def compute_result(points):
    points =[Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(1000): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
                # print("A",a)
            else:
                # add the right point
                b.add_point(point)
                # print("B",b)
        if a_old == a.points:
            break
        a_old.append(point)
        # print(a_old)
        a.update()
        b.update()
    return [(a.center.x,a.center.y),(b.center.x,b.center.y)]

points = [(1,2),(3,4),(4,5),(3,2),(1,4),(2,4),(3,1)]
print(compute_result(points))