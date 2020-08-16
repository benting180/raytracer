from vector import Vector


class Color(Vector):
    """ Store color as RGB value. """


    @classmethod
    def from_hex(cls, s):
        """ Convert #FF0000 to int 0 - 255 """
        r = int(s[1:1+2], 16) / 255.0
        g = int(s[3:3+2], 16) / 255.0
        b = int(s[5:5+2], 16) / 255.0
        return cls(r, g, b)



