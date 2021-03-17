# Tyler Percy
# 2/12/21
# PHY 2200

from vpython import *
from tank import Tank

class Interface:

    left_axis_tilt: cylinder
    left_projectile_velocity: cylinder

    left_tilt_label: label
    right_tilt_label: label
    left_vel_label: label
    right_vel_label: label

    right_axis_tilt: cylinder
    left_projectile_velocity: cylinder

    def __init__(self):
        self.left_axis_tilt = cylinder(pos = vec(-20,-17.5,0), axis = vec(1,0,0)*4, color = vec(.8,0,0), radius = .5)
        self.left_projectile_velocity = cylinder(pos = vec(-20,-19,0), axis = vec(1,0,0)*4, color = vec(1,.5,.5), radius = .5)

        self.left_tilt_label = label(pos = vec(-22.5, -17.5, 0), text = "AXIS TILT")
        self.left_vel_label = label(pos = vec(-22.5, -19, 0), text = "VELOCITY")

        self.right_tilt_label = label(pos = vec(22.5, -17.5, 0), text = "AXIS TILT")
        self.right_vel_label = label(pos = vec(22.5, -19, 0), text = "VELOCITY")

        self.right_axis_tilt = cylinder(pos = vec(20,-17.5,0), axis = vec(-1,0,0)*4, color = color.blue, radius = .5)
        self.right_projectile_velocity = cylinder(pos = vec(20,-19,0), axis = vec(-1,0,0)*4, color = color.cyan, radius = .5)

    def adjust_axis_display(self, tank):
        if tank.color == color.red:
            self.left_axis_tilt.axis.x = (3-tank.cannon.axis.x)*3
        else:
            self.right_axis_tilt.axis.x = -(tank.cannon.axis.x+3)*3

    def adjust_velocity_display(self, tank):
        if tank.color == color.red:
            self.left_projectile_velocity.axis.x = tank.bullet_v*6
        else:
            self.right_projectile_velocity.axis.x = -tank.bullet_v*6
    