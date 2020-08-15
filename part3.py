from vector import Vector
from color import Color
from image import Image
from sphere import Sphere

def main():
    
    # setting
    width = 320
    height = 200
    ar = width / height
    grey = Color(0.1,0.1,0.1)
    red = Color(1,0,0)

    # setup objects
    camera = Vector(0, 0, -1)
    sphere = Sphere(0, 0, 0, 0.5)

    # setup image
    im = Image(width, height)

    ###
    xmin = -1
    xmax = 1
    ymax = xmax / ar
    ymin = -ymax
    dx = (xmax - xmin)/(width-1)
    dy = (ymax - ymin)/(height-1)
    print("x:[{}, {}] y:[{}, {}]".format(xmin, xmax, ymin, ymax))
    z = 0
    for j in range(height):
        y = ymin + dy*j
        for i in range(width):
            x = xmin + dx*i
            end = Vector(x, y, z)
            U = end - camera # unit vector from camera to end point
            u = U.normalize()

            # calculate discriminant
            sphere2ray = sphere - camera
            a = 1
            b = 2 * u.dot(sphere2ray)
            c = sphere2ray.magnitude() - sphere.r*sphere.r
            delta = b*b - 4*a*c
            if delta < 0:
                c = grey
            else:
                c = red
            im.set_pixel(j, i, c)






    
    # iterate over pixels
    # check sphere-line interesection
    # give a color
    # im.set_pixel(j, i, color)

    im.export('sphere.ppm')
    


if __name__ == '__main__':
    main()

