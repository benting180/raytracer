from vector import Vector
from color import Color
from sphere import Sphere
from engine import Engine
from point import Point
from scene import Scene
from material import Material
from light import Light


def scene_4():
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
    sphere2 = Sphere(Point(+0.0, 0.0, 1), 0.2, material2)
    sphere3 = Sphere(Point(-0.3, 0.0, 2), 0.2, material3)
    light1 = Light(Point(10.5, -10.5, -10))
    light2 = Light(Point(10.5, 10.5, -5))
    lights = [light1, light2]
    # lights = [light1]
    objects = [sphere1, sphere2, sphere3]
    # objects = [sphere1]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    return scene

def scene_5():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, -0.35, -1)

    pink = Material(color=Color.from_hex("#803980"))
    blue = Material(color=Color.from_hex("#0000FF"))
    checker = Material(
        color1=Color.from_hex("#420500"),
        color2=Color.from_hex("#E6b87d"),
        ambient=0.2,
        reflection=0.2
    )

    
    ball_blue = Sphere(Point(+0.75, -0.1, 1), 0.6, blue)
    ball_pink = Sphere(Point(-0.75, -0.1, 2.25), 0.6, pink)
    ground = Sphere(Point(0, 10000.5, 1), 10000.0, checker)
    light1 = Light(Point(1.5, -1.5, -10.0))
    light2 = Light(Point(-0.5, -10.5, -0.0))
    lights = [light1, light2]
    # lights = [light1]
    objects = [ball_blue, ball_pink, ground]
    # objects = [sphere1]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    return scene
