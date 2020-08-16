from vector import Vector
from color import Color
from sphere import Sphere
from engine import Engine
from point import Point
from scene import Scene


def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    sphere1 = Sphere(Point(+0.3, 0.0, 0), 0.2, Color.from_hex("#FF0000"))
    sphere2 = Sphere(Point(+0.0, 0.0, 0), 0.2, Color.from_hex("#FFFF00"))
    sphere3 = Sphere(Point(-0.3, 0.0, 0), 0.2, Color.from_hex("#00FF00"))
    objects = [sphere1, sphere2, sphere3]
    scene = Scene(camera, objects, WIDTH, HEIGHT)

    engine = Engine()
    image = engine.render(scene)
    image.export('sphere2.ppm')


if __name__ == '__main__':
    main()
