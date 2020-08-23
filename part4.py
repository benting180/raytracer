import sys
from vector import Vector
from color import Color
from sphere import Sphere
from engine import Engine
from point import Point
from scene import Scene
from material import Material
from light import Light


def main(fout):
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    red = Color.from_hex("#FF0000")
    yellow = Color.from_hex("#FFFF00")
    green = Color.from_hex("#00FF00")
    ambient = Color.from_hex("#111111")
    diffuse = Color.from_hex("#FFFFFF")
    specular = Color.from_hex("#FFFFFF")
    material1 = Material(color=red)
    material2 = Material(color=yellow)
    material3 = Material(color=green)
    sphere1 = Sphere(Point(+0.3, 0.0, 0), 0.2, material1)
    sphere2 = Sphere(Point(+0.0, 0.0, 0), 0.2, material2)
    sphere3 = Sphere(Point(-0.3, 0.0, 0), 0.2, material3)
    light1 = Light(Point(10.5, -10.5, -10))
    # light2 = Light(Point(0, 0, -1))
    # lights = [light1, light2]
    lights = [light1]
    objects = [sphere1, sphere2, sphere3]
    # objects = [sphere1]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)

    engine = Engine()
    image = engine.render(scene)
    image.export(fout)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Usage:\n    python part4.py fout.ppm")
        sys.exit()
