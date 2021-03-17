# Tyler Percy
# 2/19/21
# PHY 2200

from vpython import *
from numpy import zeros

class Bullet:

    mass = 1e4
    body: sphere
    g = vec(0, -.1, 0)
    Fgrav = g*mass
    velocity: vec
    air_resist = 200

    def __init__(self, pos, vel):
        self.body = sphere(pos = pos, radius = .5, make_trail=True)
        self.velocity = vel

    def get_diffeq(self, d, tn):
        speed = mag(vec(d[3], d[4], d[5]))

        rates = zeros(6)
        rates[0] = d[3]
        rates[1] = d[4]
        rates[2] = d[5]
        rates[3] = (self.Fgrav.x-self.air_resist*speed*d[3])/self.mass
        rates[4] = (self.Fgrav.y-self.air_resist*speed*d[4])/self.mass
        rates[5] = (self.Fgrav.z-self.air_resist*speed*d[5])/self.mass
        return rates


