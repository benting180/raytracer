import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def dot(self, v):
        return self.x*v.x+self.y*v.y+self.z*v.z

    def magnitude(self):
        return math.sqrt(self.dot(self))


    def normalize(self):
        return self / self.magnitude()

    def __mul__(self, a):
        assert not isinstance(a, Vector)
        return Vector(self.x*a, self.y*a, self.z*a)

    def __rmul__(self, a):
        return  self.__mul__(a)

    def __truediv__(self, a):
        return  self.__mul__(1./a)
    
    def __add__(self, v):
        return Vector(self.x+v.x, self.y+v.y, self.z+v.z)

    def __sub__(self, v):
        return Vector(self.x-v.x, self.y-v.y, self.z-v.z)

