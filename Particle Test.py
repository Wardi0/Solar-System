from Particle import Particle

ballA = Particle([0,0,1],[0,0,0],'Ball A',1)
ballB = Particle([0,0,0],[0,0,0],'Ball B',1)
ballC = Particle([0,0,-1],[0,0,0],'Ball C',1)

balls = [ballA, ballB, ballC]

print(ballB.potentialEnergy(balls))