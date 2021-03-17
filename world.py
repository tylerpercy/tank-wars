# Tyler Percy
# 2/12/21
# PHY 2200

from vpython import *
from interface import Interface
from random import randint, uniform

class World:

    def __init__(self) -> None:
        #terrain and background
        self.scene = canvas(title = "Tank Wars", width = 1600, height = 900, range = 20, background = vec(.1,.1,.1))
        self.floor = box(pos = vec(0, -15, 0), size = vec(60, 2.5, .5), color = vec(.5,.5,.5))
        self.wall = box(pos = vec(0,-8.25,0), size = vec(1, 12, .5), color = vec(.5,.5,.5))
        self.sun = sphere(pos = vec(0,-15,-.5), size = vec(50,50,.01), color = vec(.9,.6,.2))
        self.UI = Interface()

        #stars
        for _ in range(0, 100):
            box(pos = vec(randint(-30, 30), randint(-15,15), -.6), size = vec(uniform(.15,.25), uniform(.15,.25), .05), color = color.white)

        #lock camera
        self.scene.resizable = False
        self.scene.userzoom = False
        #refocus camera
        self.scene.fov = .1

