import sys
import argparse
from vector import Vector
from color import Color
from sphere import Sphere
from engine import Engine
from point import Point
from scene import Scene
import scenes
from material import Material
from light import Light
import time


def main():
    t1 = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('fout', help="output file name")
    args = parser.parse_args()
    
    engine = Engine()
    # image = engine.render(scenes.scene_5())
    image = engine.render_multi(scenes.scene_5())
    image.export(args.fout)
    print("time spend: {:.2f} s".format(time.time()-t1))


if __name__ == '__main__':
    main()
