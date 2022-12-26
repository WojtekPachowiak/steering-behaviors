import pygame as pg
from pygame.math import Vector2



from pygame_init import SCREEN
from constant import WIDTH, HEIGHT, BACKGROUND_COLOR, COLOR

class Debug:
    debug_surf = pg.Surface((WIDTH,HEIGHT))

    def line(start:Vector2,end:Vector2, color=COLOR.RED, thickness=1):
        pg.draw.line(SCREEN,color,start, end,thickness)
        
    def circle(center:Vector2, radius:float, color=COLOR.RED, thickness=1):
        'darw debug circle. thickness=0 makes it filled'
        pg.draw.circle(SCREEN, color, center, radius,thickness)

    # def draw():
    #     SCREEN.blit(Debug.debug_surf, (0,0))
    #     Debug.debug_surf.fill(BACKGROUND_COLOR)