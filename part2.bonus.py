from image import Image
from color import Color


def main():
    red = Color(1,0,0)
    green = Color(0,1,0)
    blue = Color(0,0,1)
    yellow = red + green
    white = red + green + blue
    dark = white * 0.001

    WIDTH = 320
    HEIGHT = 200
    im = Image(width=WIDTH, height=HEIGHT)
    for j in range(HEIGHT):
        for i in range(WIDTH):
            c = Color(j/float(HEIGHT) * 1, i/float(WIDTH) * 1, j/float(HEIGHT) *0.5 + i/float(WIDTH)*0.5 )
            im.set_pixel(j, i, c)

    im.export('gradient.ppm')

if __name__ == '__main__':
    main()
