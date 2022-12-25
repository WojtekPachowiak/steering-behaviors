import pygame as pg
from overwrites import Vector2
import math
from debug import Debug
from pygame_init import SCREEN
from itertools import cycle, islice
from constant import COLOR
import utils

class LinearCyclicPath:
    'linear path'
    def __init__(self,control_points:list[Vector2]):
        self.control_points = control_points
        self.__calculate_path_length(control_points )
        
    def __calculate_path_length(self, control_points):
        "calcualtes the real length of the path and creates a dictionary mapping point's index to its normalized range (for example, 0 to (0, 0.3), 1 to (0.3, 0.75), etc.)"
        length = 0
        ranges = dict()
        n=len(control_points)
        for i in range(n):
            prev_length = length
            curr_length = control_points[i].distance_to(control_points[(i+1)%(n)]) #modulo to prevent index out of bound
            length += curr_length
            ranges[i] = (prev_length, length)
        #normalize ranges
        self.ranges = {k:(v[0]/length, v[1]/length) for k, v in ranges.items()}
        self.length = length
 
    def evaluate(self, t:float) -> Vector2:
        # modulo 1
        t, _ = math.modf(t)
        print(t)
        if t == 0:
            return self.control_points[0]
        for k, v in self.ranges.items():
            if v[0] < t and t <= v[1]:
                return self.control_points[k].lerp(self.control_points[(k+1) % len(self.control_points)], utils.remap(t,v[0],v[1],0,1))
        else:
            raise Exception("path evaluate bug")

    def draw(self):
        #draw control points
        for point in self.control_points:
            pg.draw.circle(SCREEN, COLOR.GRAY, point, 5, 1)
        #draw lines between control points
        pg.draw.aalines(SCREEN,COLOR.GRAY,True, self.control_points)


class LinearPath:
    'linear path'
    def __init__(self,control_points:list[Vector2]):
        self.control_points = control_points
        self.__calculate_path_length(control_points )
        
    def __calculate_path_length(self, control_points):
        "calcualtes the real length of the path and creates a dictionary mapping point's index to its normalized range (for example, 0 to (0, 0.3), 1 to (0.3, 0.75), etc.)"
        length = 0
        ranges = dict()
        for i in range(len(control_points)-1):
            prev_length = length
            curr_length = control_points[i].distance_to(control_points[i+1]) #modulo to prevent index out of bound
            length += curr_length
            ranges[i] = (prev_length, length)
        #normalize ranges
        self.ranges = {k:(v[0]/length, v[1]/length) for k, v in ranges.items()}
        self.length = length
 
    def evaluate(self, t:float) -> Vector2:
        #clip to (0,1)
        t = max(0, min(t,1))

        if t == 0:
            return self.control_points[0]
        for k, v in self.ranges.items():
            if v[0] < t and t <= v[1]:
                return self.control_points[k].lerp(self.control_points[k+1], t)
        else:
            raise Exception("path evaluate bug") 



