from color import Color
from vector import Vector
from image import Image
from ray import Ray
from progress import ProgressBar
class Engine:


    def __init__(self):
        pass

    def render(self, scene):
        """ Render image from stuff inside scene """
        width = scene.width
        height = scene.height
        ar = width / height

        camera = scene.camera
        im = Image(width, height)

        xmin = -1
        xmax = 1
        ymax = xmax / ar
        ymin = -ymax
        dx = (xmax - xmin)/(width-1)
        dy = (ymax - ymin)/(height-1)

        pb = ProgressBar(height*width)

        for j in range(height):
            y = ymin + dy*j
            for i in range(width):
                x = xmin + dx*i

                ray = Ray(camera, Vector(x, y, 0) - camera)
                c = self.ray_trace(ray, scene)
                im.set_pixel(j, i, c)
                pb.update(1)
        return im

    def ray_trace(self, ray, scene):
        color = Color(0.1, 0.1, 0.1)
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + dist_hit * ray.direction
        color += self.color_at(obj_hit, hit_pos, scene)
        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj

        return (dist_min, obj_hit)

    def color_at(self, obj_hit, hit_pos, scene):
        material = obj_hit.material
        base = material.base
        # 1. ambient
        ambient = material.ambient 

        # 2. diffuse
        # his_pos2light dot surface norm
        colors = Color(0,0,0)
        M = 1.0
        for light in scene.lights:
            his_pos2light = (light - hit_pos).normalize()
            hit_pos_perpen = (hit_pos - obj_hit.center).normalize()
            cos = his_pos2light.dot(hit_pos_perpen) 
            cos = 0 if cos < 0 else cos
            diffuse = cos * material.diffuse * M

            specular = Color(0,0,0)
            color = ambient + diffuse + specular
            colors += color
        return colors


        # return obj_hit.material
