from vector import Vector
import math
class Sphere(Vector):


    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        sphere2ray = ray.origin - self.center
        u = ray.direction
        a = 1
        b = 2 * u.dot(sphere2ray)
        c = sphere2ray.dot(sphere2ray) - self.radius*self.radius
        dist = None

        delta = b*b - 4*a*c
        if delta >= 0:
            dist = (-b-math.sqrt(delta))/2
            if dist > 0:
                return dist
        return None
