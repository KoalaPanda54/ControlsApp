from p5 import *
from Canvas import *
from Panel import Panel


canvas = Canvas(width, height)

panel1 = Panel(Vector(25, 25), 250, 250, 0)
panel2 = Panel(Vector(50, 50), 250, 250, -1)

canvas.add_element(panel1)
canvas.add_element(panel2)

panel2.fillColor = (200, 200, 200)
panel2.strokeColor = (100, 100, 100)

panel2.set_parent(panel1)


def setup():
    size(1280, 720)
    

def draw():
    background(0)
    ortho(-width, width, -height, height, -width, width)
    panel1.pos += Vector(frame_count/180, 0)
    camera()
    canvas.render()

run(mode='P3D')
