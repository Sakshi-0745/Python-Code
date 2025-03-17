import math
class line:
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    def distnace(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return math.sqrt((x2-x1)**2 + (y2-y1)**2) 
    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return ((y2/y1)/(x2/x1))
cord1=(14,23)
cord2= (8,2)
line = line(cord1,cord2)
print("distance",line.distnace())
print("slope",line.slope())

        