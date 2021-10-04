from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
robotArm.speed = 2
for x in range (5):
    robotArm.grab()
    for y in range (9-2*x):
        robotArm.moveRight()
    robotArm.drop()
    for z in range (8-2*x):
        robotArm.moveLeft()
robotArm.wait()