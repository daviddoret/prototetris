from prototetris_model_2 import *
from colorutils import *
from sympy import *
import pyglet

def start_app():
    """References:
    - https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/quickstart.html#hello-world
    """

    window = pyglet.window.Window()

    label = pyglet.text.Label('Hello, world',
                              font_name='Times New Roman',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2,
                              anchor_x='center', anchor_y='center')

    @window.event
    def on_draw():
        window.clear()
        label.draw()

    pyglet.app.run()