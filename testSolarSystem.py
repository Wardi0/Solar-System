from SolarSystem import solarSystem
from Planet import Body
import numpy as np

sun = Body(np.array([0,0,0]),np.array([0,0,0]),'Sun',1.989e30)
earth = Body(np.array([10000,0,0]),np.array([0,100,0]),'Earth',5.972e24)

x = [sun, earth]

earthSun = solarSystem(x)

print(earthSun) \


print(earthSun.acceleration()) \

earthSun.updateSystem(1000) \

print(earthSun) \

earthSun.updateSystem(1000) \

print(earthSun) \

