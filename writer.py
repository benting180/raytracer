class PPMWriter:
    def __init__(self, fname, data):
        self.fname = fname
        self.data = data
        self.maxv = 255
        self.check()
        self.f = open(fname, 'w')
        self.write_header_1()
        self.write_header_2()
        self.write_content()
        self.f.close()
        print("PPMWriter writing finished.")

    def check(self):
        print("PPMWriter checking...")
        self.signature = "P3"
        self.nrow = len(self.data)
        self.ncol = len(self.data[0])
        for row in self.data:
            if len(row) != self.ncol:
                raise "number of column not same for all rows"

    def write_header_1(self):
        print("PPMWriter writing header1...")
        self.f.write("# This is a comment1")
        self.f.write('\n')
        self.f.write("# This is a comment2")
        self.f.write('\n')
        items = [self.signature, self.ncol, self.nrow]
        items = [str(x) for x in items]
        line = " ".join(items)
        self.f.write(line)
        self.f.write('\n')

    def write_header_2(self):
        print("PPMWriter writing header2...")
        self.f.write("# Finally the maximum color value")
        self.f.write('\n')
        self.f.write(str(self.maxv))
        self.f.write('\n')
        pass

    def write_content(self):
        print("PPMWriter writing content...")
        self.f.write("# Content")
        self.f.write('\n')
        DELIMITER = '\t'
        for j, row in enumerate(self.data):
            for i, pix in enumerate(row):
                if i == 0:
                    # reach the begining of row
                    end = DELIMITER

                elif i == self.ncol-1:
                    # reach the end of row
                    end = '\n'

                else:
                    end = DELIMITER
                    # between the begin & the end of row
                pixv = DELIMITER.join([pix.r, pix.g, pix.b])
                self.f.write(pixv)
                self.f.write(end)


class Color:
    def __init__(self, r, g, b):

        self.r = str(r)
        self.g = str(g)
        self.b = str(b)


if __name__ == '__main__':
    p11 = Color(255, 0, 0)
    p12 = Color(0, 255, 0)
    p13 = Color(0, 0, 255)
    p21 = Color(255, 255, 0)
    p22 = Color(255, 255, 255)
    p23 = Color(0, 0, 0)
    row_1 = [p11, p12, p13]
    row_2 = [p21, p22, p23]
    rows = [row_1, row_2]
    PPMWriter('test.ppm', rows)
