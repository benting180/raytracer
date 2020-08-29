from color import Color
from vector import Vector
from image import Image
from ray import Ray
from progress import ProgressBar
import math
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

    def ray_trace(self, ray, scene, depth=0):
        color = Color.from_hex("#000000")
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + dist_hit * ray.direction
        normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, normal, ray, scene)
        if depth < 5:
            inray_dir = ray.direction
            reflect_dir = inray_dir - 2*inray_dir.dot(normal)*normal
            new_ray = Ray(hit_pos+0.00001*reflect_dir, reflect_dir)
            color += self.ray_trace(new_ray, scene, depth+1) * obj_hit.material.reflection
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

    def color_at(self, obj_hit, hit_pos, normal, ray, scene):
        material = obj_hit.material
        obj_color = obj_hit.color(hit_pos)
        # 1. ambient
        color = Color.from_hex("#FFFFFF") * material.ambient 

        to_cam = scene.camera - hit_pos

        specular_k = 50
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # 2. diffuse
            # to_light dot surface norm
            cos = max(to_light.direction.dot(normal), 0)  
            color += (
                obj_color *
                cos *
                material.diffuse
            )

            reflect = 2*cos*normal - to_light.direction
            # 3. Phong
            # color += (
            #     max((to_cam).dot(reflect.normalize()), 0)**material.specular *
            #     light.color
            # )  

            # 4. Half-way
            half_vector = (to_light.direction + to_cam).normalize()
            HR = max(half_vector.dot(normal), 0)
            color += (
                material.specular * light.color *
                HR ** specular_k
            )
        return color
