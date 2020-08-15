from image import Image
from color import Color


def main():
    red = Color(1,0,0)
    green = Color(0,1,0)
    blue = Color(0,0,1)
    yellow = red + green
    white = red + green + blue
    dark = white * 0.001

    im = Image(width=3, height=2)
    im.set_pixel(0, 0, red)
    im.set_pixel(0, 1, green)
    im.set_pixel(0, 2, blue)
    im.set_pixel(1, 0, yellow)
    im.set_pixel(1, 1, white)
    im.set_pixel(1, 2, dark)

    im.export()

if __name__ == '__main__':
    main()
