from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 5
for x in range(35):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for y in range (9):
            robotArm.moveRight()
        robotArm.drop()
        for z in range (10):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
robotArm.wait()