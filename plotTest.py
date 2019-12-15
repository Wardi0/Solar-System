import matplotlib.pyplot as plt
from SolarSystem import solarSystem
from Particle import Particle
import numpy as np

#Data from 2016-11-30
sun = Particle(np.array([5.184e8,5.567e8,-2.360e7]),np.array([-4.092,1.166e1,8.348e-2]),'Sun',1.989e30)
earth = Particle(np.array([5.584e10,1.373e11,-2.945e7]),np.array([-2.812e4,1.107e4,-8.203e-2]),'Earth',5.972e24)
mars = Particle(np.array([2.077e11,-1.358e10,-5.404e9]),np.array([2.573e3,2.626e4,4.868e2]),'Mars',6.4171e23)
moon = Particle(np.array([5.572e10,1.369e11,5.603e6]),np.array([-2.718e4,1.081e4,-9.643]),'Moon',7.349e22)
mercury = Particle(np.array([4.215e10,-4.614e10,-7.659e9]),np.array([2.668e4,3.476e4,3.917e2]),'Mercury',3.302e23)
uranus = Particle(np.array([2.751e12,1.155e12,-3.136e10]),np.array([-2.686e3,5.962e3,5.709e1]),'Uranus',86.813e24)
pluto = Particle(np.array([1.431e12,-4.758e12,9.525e10]),np.array([5.319e3,4.254e2,-1.606e3]),'Pluto',1.307e22)
saturn = Particle(np.array([-3.038e11,-1.471e12,3.766e10]),np.array([8.929e3,-1.985e3,-3.206e2]),'Saturn',5.6834e26)
venus = Particle(np.array([1.090e11,-2.099e9,-6.320e9]),np.array([7.017e2,3.486e4,4.372e2]),'Venus',48.685e23)
jupiter = Particle(np.array([-8.068e11,-1.170e11,1.853e10]),np.array([1.723e3,-1.231e4,1.257e1]),'Jupiter',1898.13e24)
neptune = Particle(np.array([4.235e12,-1.464e12,-6.745e10]),np.array([1.739e3,5.169e3,-1.460e2]),'Neptune',102.413e24)

b = [sun, earth, mars, moon, mercury, saturn, venus, jupiter, pluto, uranus, neptune]    #Add all Particle class objects to a list
timeStep = 1000     #Time step of simulation in seconds
earthSun = solarSystem(b)

plt.xlabel('x')
plt.ylabel('y')

xDict = {}  #Defines 2 empty dictionaries
yDict = {}
    
for planet in earthSun.planets:
        xDict[planet.Name] = []     #Each planet has an empty list indexed to its name for both x and y coordinates
        yDict[planet.Name] = []
        
for n in range(1000000):
    accelerationList = earthSun.acceleration()      #Calculates the ordered list of acceleration arrays 
    for i, planet in enumerate(earthSun.planets):
        if n % 50 == 0:
            xDict[planet.Name].append(planet.coordinate(0))     #Adds current x coordinate to the end of the planet's xDict list
            yDict[planet.Name].append(planet.coordinate(1))     #Adds current y coordinate to the end of the planet's yDict list
        planet.update(accelerationList[i], timeStep)        #Updates planet's position and velocity arrays

for planet in earthSun.planets: 
    plt.plot(xDict[planet.Name], yDict[planet.Name], 'r-', label = planet.Name)     #Add functionality to give unique colour to each planet

plt.legend()
plt.show()

plt.set_cmap('prism')
#plt.cm.get_cmap()
