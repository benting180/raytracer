from vector import Vector
import math
class Sphere(Vector):


    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
        if material.color1 is not None and material.color2 is not None:
            self.is_checker = True
        else:
            self.is_checker = False

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

    def normal(self, pos):
        """ for a sphere, return the unit normal vector at pos. """
        return (pos - self.center).normalize()

    def color(self, pos):
        if self.is_checker:
            return self._checker_color(pos)
        else:
            return self.material.color

    def _checker_color(self, pos):
        """ return the color from a checker board pattern. """
        # define width, height of a checker box by absolute value
        dx = 0.2
        dz = 0.2
        x, z = pos.x, pos.z
        summ = x//dx + z//dz
        if summ % 2 == 0:
            return self.material.color1
        else:
            return self.material.color2
