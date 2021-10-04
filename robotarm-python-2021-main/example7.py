from RobotArm import RobotArm
robotArm = RobotArm('exercise 7') # Jouw python instructies zet je vanaf hier:
robotArm.speed = 1 #Voor de opdracht mag je max 11 regels gebruiken maar ik heb dit erbij gezet omdat het lang duurt, als het weg MOET kan dat en dan is het 11 regels lang.
for x in range(5):
    for x in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for x in range(2):
        robotArm.moveRight()
robotArm.wait() # Na jouw code wachten tot het sluiten van de window: