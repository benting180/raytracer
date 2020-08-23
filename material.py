from color import Color
class Material:
    def __init__(self, color=Color.from_hex("#FFFFFF"), ambient=0.05, diffuse=1, specular=1):
        """
        Store the material color,
        ambient coefficient, diffuse coefficient,
        specular coefficient
        """
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
