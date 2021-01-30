from Canvas import UIObject, Canvas
from p5 import *

class Panel(UIObject):
    def __init__(self, pos : Vector, width, height, depth = 0):
        super().__init__(pos, depth)
        self.width = width
        self.height = height
        self.fillColor = (255, 255, 255)
        self.stroke = 5
        self.strokeColor = (255, 0, 255)

    def render(self):
        fill(self.fillColor[0], self.fillColor[1], self.fillColor[2])
        stroke_weight(self.stroke)
        stroke(self.strokeColor[0], self.strokeColor[1], self.strokeColor[2])
        rect(0, 0, self.width, self.height)