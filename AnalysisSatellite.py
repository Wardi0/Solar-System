import numpy as np
import matplotlib.pyplot as plt

pythonData = np.load('TwoBodyTest.npy')

def positionPlot(data):
    """
    Plots the positions of the satellite from the data file
    """
    position = plt.figure(1)
    satelliteX = []
    satelliteY = []
    
    for particleList in data:
       satelliteX.append(particleList[2].position[0])   #Appends the satellite's x-coordinate to a list
       satelliteY.append(particleList[2].position[1])   #Appends the satellite's y-coordinate to a list
       
    plt.plot(satelliteX, satelliteY, label = 'Satellite')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()    
    position.show()

def energyChangePlot(data):
    """
    Plots the change in KE of the satellite against time from the data file
    """
    energy = plt.figure(2)
    satelliteKElist = []
    time = []
    
    initialSatelliteKE = data[0][2].kineticEnergy() #Initial KE of satellite
    
    for particleList in data:
        time.append(particleList[0])    #Creates a list of time values to plot as the x-axis
        satelliteKElist.append(particleList[2].kineticEnergy() - initialSatelliteKE)
    
    plt.plot(time, satelliteKElist, label = 'Satellite')
    plt.xlabel('Time')
    plt.ylabel('Change in Kinetic Energy')
    plt.legend()    
    energy.show()

positionPlot(pythonData) 
energyChangePlot(pythonData)   
    
    
    
    
    
    
   