from constant import WIDTH, HEIGHT, FPS
import pygame as pg


pg.init()
# Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
# Set up the window.
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

class Time:
    clock = pg.time.Clock()

    def tick():
        Time.delta_time = Time.clock.tick(FPS) / 1000.0

    

