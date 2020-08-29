from color import Color
from vector import Vector
from image import Image
from ray import Ray
from progress import ProgressBar
import math
from multiprocessing import Process, Array
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

        k = 0
        eights = []
        ts = []
        eight = Array('f', 8*3)
        for j in range(height):
            y = ymin + dy*j
            for i in range(width):
                x = xmin + dx*i
                ray = Ray(camera, Vector(x, y, 0) - camera)
                k += 1
                t = Process(target=self.ray_trace_set, args=(eight, k, ray, scene))
                t.start()
                ts.append(t)


                if k == 8:
                    for t in ts:
                        t.join()
                    print("should be waiting...")

                    # done
                    eights.append(eight[:])
                    k = 0
                    ts = []
                    eight = Array('f', 8*3)


                # c = self.ray_trace(ray, scene)
                # im.set_pixel(j, i, c)
                pb.update(1)
        print(eights)
        print(len(eights))
        print(type(eights))
        new_eights = []
        for eight in eights:
            new_eights += eight

        k = 0
        for j in range(height):
            for i in range(width):
                r = new_eights[k+0]
                g = new_eights[k+1]
                b = new_eights[k+2]
                k += 3
                c = Color(r, g, b)
                im.set_pixel(j, i, c)

        return im

    def ray_trace_set(self, eight, k, ray, scene, depth=0):
        print("task {} started".format(k))
        c = self.ray_trace(ray, scene)
        i = (k-1)*3
        eight[i+0] = c.x
        eight[i+1] = c.y
        eight[i+2] = c.z
        print("task {} finished".format(k))
        return

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
