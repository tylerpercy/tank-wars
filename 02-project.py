# Tyler Percy
# 2/12/21
# PHY 2200

from world import World
from tank import Tank
from vpython import *

def main():

    map = World()

    tank1 = Tank(xpos=-20, ypos=-12.75, zpos=.5, xaxis = 1, color=color.red)
    tank2 = Tank(xpos=20, ypos=-12.75, zpos=.5, xaxis = -1, color=color.cyan)

    while(True):
        rate(100)
        tank1.move()
        if 'shift' in keysdown():
            tank1.fire(tank2)
        
        if (tank1.hit_target):
            tank2.body.visible = False
            tank2.cannon.visible = False
            break

        map.UI.adjust_axis_display(tank1)
        map.UI.adjust_velocity_display(tank1)

    print("Tank 1 wins!")
    
if __name__ == "__main__":
    main()