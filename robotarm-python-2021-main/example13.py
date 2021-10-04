from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 5
for z in range(7):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for x in range(9-1*z):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(9):
            robotArm.moveLeft()
    else:
        break
robotArm.wait()