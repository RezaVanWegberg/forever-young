from RobotArm import RobotArm
robotArm = RobotArm('exercise 3')
a = 2
for x in range (4):
    robotArm.grab()
    for y in range (a):
        robotArm.moveRight()
        a += 2
    robotArm.drop()
    for z in range (9):
        robotArm.moveLeft()
a += 2
robotArm.wait()