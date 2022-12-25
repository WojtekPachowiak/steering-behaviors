from constant import WIDTH, HEIGHT, VECTOR
import pygame as pg
from overwrites import Vector2
import math

def remap(old_val, old_min, old_max, new_min, new_max):
    return (new_max - new_min)*(old_val - old_min) / (old_max - old_min) + new_min

def get_mouse_pos():
    'return mouse position flipped on y-axis'
    pos = pg.mouse.get_pos()
    return (pos[0],HEIGHT - pos[1])


def angle_to_vec(angle:float):
    'angle (in radians) against positive x axis to orientation vector'
    return Vector2(math.cos(angle), math.sin(angle))

def vec_to_angle(vec:Vector2):
    'orientation vector to angle (in radians) against positive x axis'
    # print(math.acos(vec.normalize().dot(VECTOR.RIGHT)))
    # return math.acos(vec.normalize().dot(VECTOR.RIGHT)) * vec
    return math.radians(vec.angle_to(VECTOR.RIGHT))