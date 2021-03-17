# Tyler Percy
# 2/12/21
# PHY 2200

from world import World
from tank import Tank
from vpython import *

def main():
    t = 0
    dt = .0005

    map = World()

    tank1 = Tank(xpos=-20, ypos=-12.75, zpos=.5, xaxis = 1, color=color.red)
    tank2 = Tank(xpos=20, ypos=-12.75, zpos=.5, xaxis = -1, color=color.cyan)

    # red tank goes first
    control_tank = tank1
    enemy_tank = tank2

    while(True):
        rate(100)
        control_tank.move()
        if 'shift' in keysdown():
            control_tank.fire(enemy_tank, t, dt)

            if (control_tank.hit_target):
                enemy_tank.body.visible = False
                enemy_tank.cannon.visible = False
                break
            else:
                #swap control to other tank
                temp = control_tank
                control_tank = enemy_tank
                enemy_tank = temp

        map.UI.adjust_axis_display(control_tank)
        map.UI.adjust_velocity_display(control_tank)

        t = t + dt
    
if __name__ == "__main__":
    main()
