from vector import Vector
class Sphere(Vector):
    def __init__(self, x, y, z, r):
        super().__init__(x, y, z)
        # self.x = x
        # self.y = y
        # self.z = z
        self.r = r
