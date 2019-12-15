import numpy as np
import matplotlib.pyplot as plt
from SolarSystem import solarSystem
from Particle import Particle
import math

G = 6.67408E-11
earthMass = 5.97237e24   # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710*1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(np.array([0,0,0]), np.array([0,10,0]),'Earth', earthMass)
satPosition = earthRadius+(35786*1e3)
satVelocity = math.sqrt(G*Earth.mass/(satPosition))
Satellite = Particle([satPosition,0,0], [0,satVelocity,0], "Satellite", 100)

b = [Earth, Satellite]    #Add all Particle class objects to a list
plt.xlabel('x')
plt.ylabel('y')
        
earthSatellite = solarSystem(b)
        
print

