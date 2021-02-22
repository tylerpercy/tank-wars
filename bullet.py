# Tyler Percy
# 2/19/21
# PHY 2200

from vpython import *

class Bullet:

    mass = .1
    body = sphere
    g = vec(0, -9.8, 0)
    Fnet = g*mass
    momentum = vec(0,0,0)

    def __init__(self, pos, vel):
        self.body = sphere(pos = pos, radius = .5, make_trail=True)
        self.velocity = vel
        self.momentum = self.velocity*self.mass
