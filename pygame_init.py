from constant import WIDTH, HEIGHT, FPS, BACKGROUND_COLOR
import pygame as pg
from imgui.integrations.pygame import PygameRenderer
import imgui
import OpenGL.GL as gl
import numpy as np
import ctypes

pg.init()
pg.display.set_mode((WIDTH, HEIGHT), pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE) # |pygame.FULLSCREEN

#imgui
imgui.create_context()
impl = PygameRenderer()
io = imgui.get_io()
io.display_size = (WIDTH, HEIGHT) 


class Time:
    clock = pg.time.Clock()
    delta_time =  1/FPS 

    def tick():
        Time.delta_time = Time.clock.tick(FPS) / 1000.0


class Screen:
    pg_screen = pg.Surface((WIDTH, HEIGHT)) 
    screen_tex:int 
    vao: int

    def clear():
        r,g,b = BACKGROUND_COLOR
        gl.glClearColor(r/255., g/255., b/255., 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)



    # def __pygame_surf_to_opengl():
    #     # load texture
    #     surf = pg.image.tostring(Screen.pg_screen, 'RGB')
    #     texID = gl.glGenTextures(1)
    #     gl.glBindTexture(gl.GL_TEXTURE_2D, texID)
    #     gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    #     gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
    #     gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP)
    #     gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP)
    #     gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, WIDTH, HEIGHT, 0, gl.GL_RGB, gl.GL_UNSIGNED_BYTE, surf)
    #     gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
    def setup():
        Screen.__setup_screenquad()


    def __setup_screenquad():
        '''add a quad that fills the entire screen'''
        #buffer in Normalized Device Coordinates
        vertices = np.array([ 
            #positions   #texCoords
            -1.0,  1.0,  0.0, 1.0,
            -1.0, -1.0,  0.0, 0.0,
            1.0, -1.0,  1.0, 0.0,

            -1.0,  1.0,  0.0, 1.0,
            1.0, -1.0,  1.0, 0.0,
            1.0,  1.0,  1.0, 1.0
        ],dtype=np.float32)
        vao = gl.glGenVertexArrays(1)
        vbo = gl.glGenBuffers(1)
        gl.glBindVertexArray(vao)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0);
        gl.glVertexAttribPointer(0, 2, gl.GL_FLOAT, gl.GL_FALSE, 4 * vertices.itemsize, ctypes.c_void_p(0));
        gl.glEnableVertexAttribArray(1);
        gl.glVertexAttribPointer(1, 2, gl.GL_FLOAT, gl.GL_FALSE, 4 * vertices.itemsize, ctypes.c_void_p(8));
        gl.glBindVertexArray(0)
        Screen.vao = vao

        # load texture
        img = pg.image.load('walter.jpg')
        surf = pg.image.tostring(img, 'RGBA')
        tex = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, tex)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP)
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, img.get_width(), img.get_height(), 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, surf)
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        Screen.screen_tex = tex


    def handle_events(event:pg.event.Event  ):
        if event.type == pg.VIDEORESIZE:
            gl.glViewport(0, 0, event.w, event.h)
        impl.process_event(event)

    def update_UI():
        imgui.new_frame()
    
    def render():

        #render opengl screen texture
        gl.glBindVertexArray(Screen.vao)
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 6)

        #render imgui UI
        imgui.render()
        impl.render(imgui.get_draw_data())

        # #flip y axis
        # Screen.gl_screen.blit(pg.transform.flip(Screen.gl_screen,False, True), (0, 0))

        pg.display.flip()
    
Screen.setup()



def agent_UI():
    if imgui.begin_main_menu_bar():
        if imgui.begin_menu("File", True):

            clicked_quit, selected_quit = imgui.menu_item(
                "Quit", 'Cmd+Q', False, True
            )

            if clicked_quit:
                exit(1)

            imgui.end_menu()
        imgui.end_main_menu_bar()

    imgui.show_test_window()

    imgui.begin("Agent", True)
    imgui.text("Bar")
    imgui.text_colored("Eggs", 0.2, 1., 0.)
    imgui.end()