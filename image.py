class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, y, x, color):
        self.pixels[y][x] = color

    def export(self, fname='image2.ppm'):
        def to_byte(v):
            return max(min(round(v*255), 255), 0)

        with open(fname, 'w') as f:
            f.write('P3 {} {}\n255\n'.format(self.width, self.height))
            for row in self.pixels:
                for pix in row:
                    f.write('{} {} {} '.format(to_byte(pix.x), to_byte(pix.y), to_byte(pix.z)))
                f.write('\n')


