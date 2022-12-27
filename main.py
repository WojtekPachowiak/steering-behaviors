from pygame_init import Screen, Time
import sys
import pygame as pg
from constant import WIDTH,HEIGHT, FPS
from pygame.math import Vector2


import ctypes

import math
# from agent import Agent
# from paths import LinearCyclicPath, LinearPath

import utils

# from debug import Debug











# agent = Agent()

# objects = [Agent()]
# path = LinearCyclicPath([Vector2(50,50), Vector2(100, 400), Vector2(400,500), Vector2(500,100)])


running = True
while running: 
    ######## update
    for event in pg.event.get():
        if event.type == pg.QUIT or  (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False
        Screen.handle_events(event)


    Time.tick()
    
    # t = utils.get_mouse_pos()[0]/WIDTH

    # agent.seek(path.evaluate(t))
    # agent.update()
    
    Screen.update_UI()
    
    ####### rendering
    Screen.clear()
    

    # path.draw()
    # agent.draw()
    
    Debug.circle(utils.get_mouse_pos(), 10, thickness=1)


    Screen.render()
pg.quit()
    

