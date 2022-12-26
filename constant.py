WIDTH, HEIGHT = 800, 800
FPS = 60

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

BACKGROUND_COLOR = COLOR.BLACK

class VECTOR:
    from pygame.math import Vector2



    UP = Vector2(0,1)
    RIGHT = Vector2(1,0)