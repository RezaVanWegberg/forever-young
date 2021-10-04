from ctypes import memmove
from typing import Collection
from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2
for z in range(9):
    robotArm.moveRight()
for x in range(10):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()
robotArm.wait()