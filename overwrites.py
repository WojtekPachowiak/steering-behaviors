import pygame as pg

class Vector2(pg.math.Vector2):
    "pygame's Vector2 class overwrite"

    #when vector is (0,0). then return (0,0) and don't throw an error
    def normalize(self):
        print("chuj")
        try:
            return super().normalize()
        except ValueError:
            return Vector2(0,0)

print(Vector2.__dict__)
print(pg.math.Vector2.__dict__)

