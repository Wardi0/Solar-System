import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from SolarSystem import solarSystem

def positionPlot(data):
    """
    Plots the x,y positions of the system from the data file
    
    data = Imported .npy file
    """
    position = plt.figure(1)
    xDict = {}  #Defines 2 empty dictionaries
    yDict = {}
    plt.xlabel('x')
    plt.ylabel('y')
    
    for n in range(1, len(data[0])):
        xDict[data[0][n].Name] = []     #Each particle has an empty list indexed to its name for both x and y coordinates
        yDict[data[0][n].Name] = []
    
    for particleList in data:
        for n in range(1, len(data[0])):    #Goes through each particle and adds its x and y coordinate to their own lists in the dictionaries
            xDict[particleList[n].Name].append(particleList[n].position[0])
            yDict[particleList[n].Name].append(particleList[n].position[1])
            
    for n in range(1, len(data[0])):    #Plots each list in the dictionaries
        plt.plot(xDict[data[0][n].Name], yDict[data[0][n].Name], label = data[0][n].Name)
    
    plt.legend()    
    position.show()
    
def energySystemChangePlot(data, plotLabel):
    """
    Plots the percentage change in mechanical energy of the system against time from the data file
    
    data = Imported .npy file
    
    plotLabel = Label for the plot in the legend
    """
    percentage = 0
    energySystemPlot = plt.figure(3)
    time = []
    totalElist = []
    initialSystem = solarSystem(data[0][1:])
    initialSystemE = initialSystem.systemKE() + initialSystem.systemPE()    #Assigns initial mechanical energy as a variable for use in percentage change calculation
    
    for n, particleList in enumerate(data):
        time.append(particleList[0])    #Adds the time value to a list for use as x values
        system = solarSystem(particleList[1:])      #Creates a solarSystem object out of each list so class methods can be called
        totalE = system.systemKE() + system.systemPE()
        totalElist.append(100*((totalE/initialSystemE)-1))      #Converts the current mechanical energy into a percentage change
        if (n % (len(data)//100)) == 0:     #Prints the percentage of steps completed
            percentage = percentage + 1
            print(percentage, '% Progress')
    
    print('Max:',max(totalElist))
    print('Min:',min(totalElist))   #Prints the minimun, maximum and mean
    print('Mean:',stat.mean(totalElist))
    
    coefficient = np.polyfit(time,totalElist,1)
    print('Linear Coefficient:', coefficient)
    
    plt.plot(time, totalElist, label = str(plotLabel))
    plt.xlabel('Time')
    plt.ylabel('Percentage change in Mechanical Energy of the System')
    plt.legend()    
    energySystemPlot.show()
    
def virialTheoremPlot(data, plotLabel):
    """
    Plots the percentage change of the quantity 2T-U of the system against time from the data file
    
    T = Total kinetic energy of the system

    U = Total potential energy of the system
    
    data = Imported .npy file
    
    plotLabel = Label for the plot in the legend
    """
    percentage = 0
    virialPlot = plt.figure(1)
    time = []
    energyList = []
    initialSystem = solarSystem(data[0][1:])
    initial = 2*initialSystem.systemKE() - initialSystem.systemPE()     ##Assigns initial 2T-U as a variable for use in percentage change calculation
    
    for n, particleList in enumerate(data):
        time.append(particleList[0])
        system = solarSystem(particleList[1:])  #Creates a solarSystem object out of each list so class methods can be called
        energyList.append(100*(((2*system.systemKE()-system.systemPE())/initial)-1))    #Converts the current 2t-U into a percentage change
        if (n % (len(data)//100)) == 0:     #Prints the percentage of steps completed
            percentage = percentage + 1
            print(percentage, '% Progress')
                
    print('Max:',max(energyList))
    print('Min:',min(energyList))   #Prints the minimun, maximum and mean
    print('Mean:',stat.mean(energyList))
        
    plt.plot(time, energyList, label = str(plotLabel))
    plt.xlabel('Time (seconds)')
    plt.ylabel('Percentage Change in 2T - U of the System')
    plt.legend()
    virialPlot.show()
    
def linearMomentumSystemChangePlot(data, plotLabel, coordinate):
    """
    Plots the percentage change in linear momentum of the system against time from the data file
    
    data = Imported .npy file
    
    plotLabel = Label for the plot in the legend
    
    coordinate = Component of the linear momentum to be plotted (x=0)(y=0)(z=0)
    """
    momentumSystemPlot = plt.figure(4)
    percentage = 0
    time = []
    totalMlist = []
    initialSystem = solarSystem(data[0][1:])
    initialSystemM = initialSystem.systemLinearMomentum()[int(coordinate)]      ##Assigns initial linear momentum as a variable for use in percentage change calculation
    
    for n, particleList in enumerate(data):
        time.append(particleList[0])    #Adds the time value to a list for use as x values
        system = solarSystem(particleList[1:])      #Creates a solarSystem object out of each list so class methods can be called
        totalM = system.systemLinearMomentum()[int(coordinate)]
        totalMlist.append(100*((totalM/initialSystemM)-1))      #Converts the current linear momentum into a percentage change
        if (n % (len(data)//100)) == 0:     #Prints the percentage of steps completed
            percentage = percentage + 1
            print(percentage, '% Progress')
                
    print('Max:',max(totalMlist))
    print('Min:',min(totalMlist))   #Prints the minimun, maximum and mean
    print('Mean:',stat.mean(totalMlist))
    
    coefficient = np.polyfit(time,totalMlist,1)
    print('Linear Coefficient:', coefficient)
    
    plt.plot(time, totalMlist, label = str(plotLabel))
    plt.xlabel('Time')
    plt.ylabel('Percentage change in Linear Momentum of the System')
    plt.legend()    
    momentumSystemPlot.show()
    
def angularMomentumSystemChangePlot(data, plotLabel, coordinate):
    """
    Plots the percentage change in angular momentum of the system against time from the data file
    
    data = Imported .npy file
    
    plotLabel = Label for the plot in the legend
    
    coordinate = Component of the linear momentum to be plotted (x=0)(y=0)(z=0)
    """
    angMomentumSystemPlot = plt.figure(4)
    percentage = 0
    time = []
    totalMlist = []
    initialSystem = solarSystem(data[0][1:])
    initialSystemM = initialSystem.systemAngularMomentum()[int(coordinate)]     ##Assigns initial angular momentum as a variable for use in percentage change calculation
    
    for n, particleList in enumerate(data):
        time.append(particleList[0])    #Adds the time value to a list for use as x values
        system = solarSystem(particleList[1:])      #Creates a solarSystem object out of each list so class methods can be called
        totalM = system.systemAngularMomentum()[int(coordinate)]
        totalMlist.append(100*((totalM/initialSystemM)-1))      #Converts the current angular momentum into a percentage change
        if (n % (len(data)//100)) == 0:     #Prints the percentage of steps completed
            percentage = percentage + 1
            print(percentage, '% Progress')
                
    print('Max:',max(totalMlist))
    print('Min:',min(totalMlist))   #Prints the minimun, maximum and mean
    print('Mean:',stat.mean(totalMlist))
    
    coefficient = np.polyfit(time,totalMlist,1)
    print('Linear Coefficient:', coefficient)
    
    plt.plot(time, totalMlist, label = str(plotLabel))
    plt.xlabel('Time')
    plt.ylabel('Percentage change in Angular Momentum of the System')
    plt.legend()    
    angMomentumSystemPlot.show()

    
    
   