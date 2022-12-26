import pygame as pg

class Vector2(pg.math.Vector2):
    "pygame's Vector2 class overwrite"

    def __init__(self, a,b) :
        return super().__init__(a,b)

    #when vector is (0,0). then return (0,0) and don't throw an error
    def normalize(self):
        print("chuj")
        try:
            a = super().normalize()
            return 5.
        except ValueError:
            return Vector2(0,0)

