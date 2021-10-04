from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:

for x in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

#Ik weet nu wel hoe je het vaker laat doen
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()