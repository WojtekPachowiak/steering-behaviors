from pygame_init import SCREEN, Time
import sys
import pygame as pg
from constant import WIDTH,HEIGHT, FPS
from pygame.math import Vector2



import math
from agent import Agent
from paths import LinearCyclicPath, LinearPath

import utils

from debug import Debug

# from imgui.integrations.pygame import PygameRenderer
# import imgui





        
        



agent = Agent()

# objects = [Agent()]
path = LinearCyclicPath([Vector2(50,50), Vector2(100, 400), Vector2(400,500), Vector2(500,100)])


# imgui.create_context()
# impl = PygameRenderer()
# io = imgui.get_io()
# io.display_size = (WIDTH, HEIGHT)
        
    



dt = 1/FPS # dt is the time since last frame.
while True: 
    ######## update
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit() 
            sys.exit() 
        # impl.process_event(event)

    # imgui.new_frame()

    Time.tick()
    
    t = utils.get_mouse_pos()[0]/WIDTH

    agent.seek(path.evaluate(t))
    agent.update()
    
    
    

    ####### rendering
    SCREEN.fill((0, 0, 0)) 

    path.draw()
    agent.draw()
    
    Debug.circle(utils.get_mouse_pos(), 10, thickness=1)

    # Debug.draw()

    #flip y axis
    SCREEN.blit(pg.transform.flip(SCREEN,False, True), (0, 0))
    pg.display.flip()


pg.quit()
    

