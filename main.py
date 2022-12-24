from enum import Enum,auto
import sys
import pygame as pg
from pygame.math import Vector2
from constant import WIDTH,HEIGHT

def get_mouse_pos():
    'return mouse position flipped on y-axis'
    pos = pg.mouse.get_pos()
    return (pos[0],HEIGHT - pos[1])

class COLOR:
    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)


class Agent:
    def __init__(self, position = Vector2(0,0), size = (50,50), color = COLOR.CYAN):
        self.surf = pg.Surface(size)
        # self.rect = pg.draw.circle(self.surf, color, (25,25), 10 )

        #bottom-left, top-middle, bottom-right
        triangle_vertex_coords = ((0,0),(size[0]/2, size[1]),(size[0],0)) 

        pg.draw.polygon(self.surf, color, triangle_vertex_coords)
        self.surf.set_colorkey(COLOR.BLACK)
        self.angle = 0
        self.pos = position
        self.vel = Vector2(0,1)
        self.acc = Vector2(0,0)
        self.max_vel_mag = 10
        self.max_acc_mag = 10
        self.mass = 1

    def move_local(self, forward, right):
        pass

    def move_world(self, dir:Vector2):
        pass
    
    def update(self):
        self.pos += self.vel
        self.vel += self.acc

    def rotate(self, angle:float):
        'rotate counterclockwise in degrees (not radians!)'
        self.angle  = (self.angle + angle) % 360

    def draw(self, surf:pg.Surface):
        #apply rotation
        final_surf = pg.transform.rotate(self.surf, self.angle)
        final_pos = (
            final_surf
            .get_rect()
            .move( -final_surf.get_width()/2, -final_surf.get_height()/2 )
        )

        #apply position
        final_pos.center = self.pos

        surf.blit(final_surf, final_pos)

    def seek(self, target_pos:Vector2):
        desired_vel = (target_pos - self.pos).normalize() * self.max_vel_mag
        self.acc = (desired_vel - self.vel).normalize() * self.max_acc_mag

        
        



# surf = pg.Surface((50,50))
# rect = pg.draw.circle(surf, (0,255,255), (25,25), 10 )  
# # rect = pg.draw.polygon(surf, (0, 255, 255), ((25,75),(320,125),(250,375)))
# self.screen.blit(surf, rect.move(110,130))


class Simulation:
    
    def __init__(self) -> None:
        pg.init()
        # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
        self.FPS = 60.0
        self.clock = pg.time.Clock()
        # Set up the window.
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))


        
        self.objects = [Agent()]


    def update(self, dt):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit() 
                sys.exit() 
        
        for obj in self.objects:
            obj.seek(get_mouse_pos())
            obj.update()

    def draw(self, screen):
        screen.fill((0, 0, 0)) 

        for obj in self.objects:
            obj.draw(screen)

        #flip y axis
        screen.blit(pg.transform.flip(self.screen,False, True), (0, 0))

        pg.display.flip()

    def run(self):
        dt = 1/self.FPS # dt is the time since last frame.
        while True: 
            self.update(dt) 
            self.draw(self.screen)
            
            dt = self.clock.tick(self.FPS)


Simulation().run()