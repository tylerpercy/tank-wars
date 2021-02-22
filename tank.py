# Tyler Percy
# 2/12/21
# PHY 2200

from vpython import *
from bullet import Bullet

class Tank:

    body = box
    cannon = cylinder
    pos = vec(0,0,0)
    color = color.red

    const_v = .05
    axis_rotate_scale = .02
    
    current_bullet = sphere
    bullet_v = .5
    hit_target = False

    def __init__(self, xpos, ypos, zpos, xaxis, color):
        self.body = box(pos = vec(xpos, ypos, zpos), size = vec(2,2,.5), color = color)
        self.cannon = cylinder(pos = vec(xpos, ypos+.75, zpos), color = color, axis = vec(xaxis,1,0)*2, radius = .5)
        self.color = color

    def move(self):
        k = keysdown()
        if 'left' in k:
            self.body.pos.x -= self.const_v
            self.cannon.pos.x -= self.const_v
        if 'right' in k:
            if self.cannon.pos.x < -3.5 or self.cannon.pos.x > 3.5:
                self.body.pos.x += self.const_v
                self.cannon.pos.x += self.const_v
        if 'up' in k:
            if self.cannon.axis.x > 1:
                self.cannon.axis.y += self.axis_rotate_scale
                self.cannon.axis.x -= self.axis_rotate_scale
        if 'down' in k:
            if self.cannon.axis.x < 3:
                self.cannon.axis.y -= self.axis_rotate_scale
                self.cannon.axis.x += self.axis_rotate_scale
        if 'w' in k:
            if -.05 <= self.bullet_v < 1:
                self.bullet_v += .005
        if 's' in k:
            if 0 < self.bullet_v <= 1.05:
                self.bullet_v -= .005

    def fire(self, target):
        self.current_bullet = Bullet(pos=vec(self.cannon.pos.x+.5, self.cannon.pos.y+.5, self.cannon.pos.z), \
                vel=vec(self.bullet_v*self.cannon.axis.x, self.bullet_v*self.cannon.axis.y, 0))

        while (self.current_bullet.body.pos.y > -21):
            if target.body.pos.x-1 < self.current_bullet.body.pos.x < target.body.pos.x+1 and \
                target.body.pos.y-1 < self.current_bullet.body.pos.y < target.body.pos.y+1:
                    print("Target hit")
                    self.hit_target = True
                    break

            # replace with ODE solver (RK4)
            self.current_bullet.body.pos += (self.current_bullet.momentum / self.current_bullet.mass) * .0001
            self.current_bullet.momentum += self.current_bullet.Fnet * .000001

        self.current_bullet.body.clear_trail()
        self.current_bullet.body.visible = False
    



