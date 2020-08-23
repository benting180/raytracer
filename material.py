from color import Color
class Material:
    def __init__(self, color=Color.from_hex("#FFFFFF"),
                 color1 = None,
                 color2 = None,
                 ambient=0.05,
                 diffuse=1,
                 specular=1,
                 reflection=0.2
             ):
        """
        Store the material color,
        ambient coefficient, diffuse coefficient,
        specular coefficient
        color1, color2 for checkerboard pattern
        """
        self.color = color
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection
