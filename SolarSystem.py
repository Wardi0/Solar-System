import numpy as np
import matplotlib.pyplot as plt
import copy

class solarSystem:
    """
    Takes a list of particle-class objects and calculates the properties of the system at the current
    time while also estimating the arrangement of this system at later times
    
    Ensure all inputted names and positions are unique
    """
    def __init__(self, planets):    #Input is a list of Particle-type objects
        self.planets = planets

    def __repr__(self):
        return '{}'.format(self.planets)       
            
    def livePlot(self, timeStep, steps, plotJumps, plotPause, method):
        """
        Plots the positions of the system of particles in "real time" (simultaneous positions of particle plotted at the same time)
        
        timeStep = Time in seconds between each recalculation of each particles position, velocity and acceleration
        
        steps = Number of steps the system is simulated for; Total time of simulation is timeStep*steps
        
        plotJumps = Number of steps calculated between each plot point
        
        plotPause = Duration of real time pause in seconds between the plotting of succesive points
        
        method = Approximation method used ('E' - Euler method) ('EC' - Euler-Cromer method) ('ER' - Euler-Richardson method)
        """
        percentage = 0
        plt.xlabel('x')
        plt.ylabel('y')
        for n in range(steps):
            systemInitial = copy.deepcopy(self.planets)     #Copies initial system state for use in acceleration calculations
            for planet in self.planets:     
                if n % plotJumps == 0:      #Only plots point if step number is an integer multiple of stepJumps
                    plt.scatter(planet.position[0],planet.position[1],s = 1, c = 'r')
                planet.update(systemInitial, timeStep, method) #Updates planet's position and velocity arrays
            if n % plotJumps == 0:
                plt.pause(plotPause)    #Pauses the program temporarily after plotting each set of points
            if (n % (steps//100)) == 0:     #Prints the percentage of steps completed
                percentage = percentage + 1
                print(percentage, '% Progress')
                
    def exportPlotData(self, timeStep, steps, plotJumps, fileName, method):
        """
        Exports a list of the system's particle's properties at a given time as a .npy file
        
        timeStep = Time in seconds between each recalculation of each particles position, velocity and acceleration
        
        steps = Number of steps the system is simulated for; Total time of simulation is timeStep*steps
        
        plotJumps = Number of steps calculated between each time that is exported
        
        fileName = Name of exported data file
        
        method = Approximation method used ('E' - Euler method) ('EC' - Euler-Cromer method) ('ER' - Euler-Richardson method)
        """
        percentage = 0
        time = 0    #Initial time is 0
        Data   = []     #Data set is initiallly empty
        for n in range(steps):
            systemInitial = copy.deepcopy(self.planets)     #Copies initial system state for use in acceleration calculations
            if n % plotJumps == 0:
                item = [time]                           #Only stores data if step number is an integer multiple of stepJumps
            for planet in self.planets:
                if n % plotJumps == 0:                  #Only stores data if step number is an integer multiple of stepJumps
                    item.append(copy.deepcopy(planet))                      
                planet.update(systemInitial, timeStep, method)        #Updates planet's position and velocity arrays
            if (n % (steps//100)) == 0:     #Prints the percentage of steps completed
                percentage = percentage + 1
                print(percentage, '% Progress')
            time = time + timeStep 
            Data.append(item)
        np.save(str(fileName), Data)
                
    def linePlot(self, timeStep, steps, plotJumps, method):
        """
        Plots the positions of the system of particles as continuous lines
        
        timeStep = Time in seconds between each recalculation of each particles position, velocity and acceleration
        
        steps = Number of steps the system is simulated for; Total time of simulation is timeStep*steps
        
        plotJumps = Number of steps calculated between each plot point
        
        method = Approximation method used ('E' - Euler method) ('EC' - Euler-Cromer method) ('ER' - Euler-Richardson method)
        """
        xDict = {}  #Defines 2 empty dictionaries
        yDict = {}
        percentage = 0
        plt.xlabel('x')
        plt.ylabel('y')
        for planet in self.planets:    #Add all particle class objects to a list
            xDict[planet.Name] = []     #Each planet has an empty list indexed to its name for both x and y coordinates
            yDict[planet.Name] = []
        for n in range(steps):
            systemInitial = copy.deepcopy(self.planets)     #Copies initial system state for use in acceleration calculations
            for planet in self.planets:
                if n % plotJumps == 0:      #Only plots point if step number is an integer multiple of stepJumps
                    xDict[planet.Name].append(planet.position[0])     #Adds current x coordinate to the end of the planet's xDict list
                    yDict[planet.Name].append(planet.position[1])     #Adds current y coordinate to the end of the planet's yDict list
                planet.update(systemInitial, timeStep, method)        #Updates planet's position and velocity array
            if (n % (steps//100)) == 0:     #Prints the percentage of steps completed
                percentage = percentage + 1
                print(percentage, '% Progress')
        for planet in self.planets: 
                plt.plot(xDict[planet.Name], yDict[planet.Name], label = planet.Name)
        plt.legend()
        plt.show()
        
    def systemPE(self):
        """
        Returns the total gravitational potential energy of the system
        """
        totalPE = 0
        for n in range(len(self.planets)):
            totalPE = totalPE + self.planets[n].potentialEnergy(self.planets[n:]) #[n:] Prevents double counting of any particle's PE
        return totalPE
    
    def systemKE(self):
        """
        Returns the total kinetic energy of the system
        """
        totalKE = 0
        for particle in self.planets:
            totalKE = totalKE + particle.kineticEnergy()    #Adds up the kinetic energy of each particle in the system
        return totalKE
    
    def systemLinearMomentum(self):
        """
        Returns the total linear momentum of the system
        """
        totalMomentum = np.array([0,0,0])
        for particle in self.planets:
            totalMomentum = totalMomentum + particle.linearMomentum()   #Adds up the linear momentum of each particle in the system
        return totalMomentum
    
    def systemAngularMomentum(self):
        """
        Returns the total angular momentum of the system
        """
        totalMomentum = np.array([0,0,0])
        for particle in self.planets:
            totalMomentum = totalMomentum + particle.angularMomentum()   #Adds up the angular momentum of each particle in the system
        return totalMomentum
        
        
    planets = []
            
            
