import pygame as pg
from pygame.math import Vector2



from constant import COLOR, FPS
import utils
import math
from debug import Debug
from pygame_init import SCREEN, Time


class Agent(pg.Surface):
    def __init__(self,position = Vector2(0,0), size = (50,50), color = COLOR.CYAN):
        self.surf = pg.Surface(size)
        # self.rect = pg.draw.circle(self.surf, color, (25,25), 10 )

        #bottom-left, top-middle, bottom-right
        triangle_vertex_coords = ((0,size[1]),(size[0], size[1]/2),(0,0)) 

        pg.draw.polygon(self.surf, color, triangle_vertex_coords)
        self.surf.set_colorkey(COLOR.BLACK)
        self.angle = 0
        self.pos = position
        self.vel = Vector2(0.,0.)
        self.acc = Vector2(0.,0.)
        self.max_speed = 200.
        self.max_acc_mag = 50
        self.mass = 1.
        self.facing_rotation_speed = 10.

    def move_local(self, forward, right):
        pass

    def move_world(self, dir:Vector2):
        pass
    
    def update(self):
        self.vel += self.acc * Time.delta_time 
        self.pos += self.vel * Time.delta_time 


    def rotate(self, angle:float):
        'rotate counterclockwise in degrees (not radians!)'
        self.angle  = (self.angle + angle)

    def draw(self):

        #apply facing direction
        self.angle = utils.vec_to_angle(self.vel)

        #apply rotation
        final_surf = pg.transform.rotate(self.surf, math.degrees(self.angle))
        final_pos = (
            final_surf
            .get_rect()
            .move( -final_surf.get_width()/2, -final_surf.get_height()/2 )
        )

        #apply position
        final_pos.center = self.pos

        SCREEN.blit(final_surf, final_pos)

        debug_scale=50
        Debug.line(self.pos, self.vel*debug_scale + self.pos, color=COLOR.GREEN,thickness=5)
        Debug.line(self.vel*debug_scale, self.acc*debug_scale + self.vel*debug_scale, color= COLOR.BLUE, thickness=5)


        
    def seek(self, target_pos:Vector2, slow_radius=False) -> Vector2: 
        #vector to target    
        pos_diff = (target_pos - self.pos)

        # if pos_diff.magnitude() > self.max_vel_mag:

        #calculate desired speed
        desired_speed = self.max_speed
        if (slow_radius):
            radius = 100    
            distance = pos_diff.length()
            if distance < radius:
                desired_speed = utils.remap(distance, 0, radius, 0, self.max_speed)
        
        #rename "vector to target" as "desired velocity"
        desired_vel = pos_diff
        desired_vel.scale_to_length(desired_speed)
        vel_diff = (desired_vel - self.vel)
        if vel_diff.magnitude() > self.max_acc_mag:
            vel_diff.scale_to_length(self.max_acc_mag)

        #rename "velocity difference" as "desired acceleration"
        desired_acc = vel_diff
        return desired_acc
        

    def flee(self, target_pos:Vector2) -> Vector2:
        'reversed seek'
        return self.seek(target_pos) * -1
    
    def arrive(self, target_pos:Vector2) -> Vector2:
        'seek with slow radius applied'
        return self.seek(target_pos, slow_radius=True)

    def wander(self, target_pos:Vector2) -> Vector2:
        'smooth brownian motion :D'
        return 0

    def evade():
        pass

    def pursue():
        pass

    def follow_path():
        pass

    def evade_obstacles():
        pass


