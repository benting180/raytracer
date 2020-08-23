from color import Color
from vector import Vector
class Light:
    """ Store position and color of light source. """
    def __init__(self, position, color=Color.from_hex("#FFFFFF")):
        self.position = position
        self.color = color
                 

