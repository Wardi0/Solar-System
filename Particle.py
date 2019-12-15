import scipy.constants as scp
import numpy as np

class Particle:
    """
    A class that takes the initial state of a particle and estimate it's properties at a later
    time using various numerical methods
    """
 
    def __init__(self, initialPosition, initialVelocity, Name, mass):   
        self.position = np.array(initialPosition, dtype=float)      #Ensures position instance variable is a NumPy array
        self.velocity = np.array(initialVelocity, dtype=float)      #Ensures velocity instance variable is a NumPy array
        self.Name = Name
        self.mass = mass
    
    def __repr__(self):
        return 'Name: {}, Mass: {}, Position: {}, Velocity: {}'.format(self.Name, self.mass, self.position, self.velocity)
    
    def gravity(self, otherParticlePositon):
        """
        Returns the acceleration of another particle due to the gravitational field of the particle
        
        otherParticlePosition = Position vector of the other particle from the same origin as self
        """
        positionVector = otherParticlePositon - self.position    #Vector from self to the other particle
        squareSum = 0
        for i in positionVector:    #Calculates the magnitude of positionVector dotted with itself
            squareSum += i**2
        positionVectorAbs = np.sqrt(squareSum)      #Gives the magnitude of positionVector
        return ((-scp.gravitational_constant)*self.mass*positionVector/(positionVectorAbs**3))      #Returns the acceleration of the other pqrticle caused by self 
    
    def acceleration(self, system, position):
        """
        Returns an array that describe the acceleration of the particle due to the gravitational forces of other particles in the system
        
        system = The solarSystem-class object (or a list of particle-class objects) in the system being simulated
        
        position = The position of the particle at which its acceleration is being calculated
        """
        netGravity = np.array([0,0,0])
        for particle in system:    
            if self.Name != particle.Name:  #Prevents program calculating gravitational effect of a particle on itself
                netGravity = netGravity + particle.gravity(position)    #Sums contribution of each particle
        return netGravity
    
    def update(self, system, deltaT, method):
        """
        Updates the position and velocity of the object to an estimate of these properties after a time deltaT

        system = The solarSystem-class object (or a list of particle-class objects) in the system being simulated
        
        deltaT = Time forward that is estimated
        
        method = Approximation method used ('E' - Euler method) ('EC' - Euler-Cromer method)
        """
        if method == 'E':   #Euler Method
            self.position = self.position + self.velocity*deltaT    #Update position first using the initial velocity
            self.velocity = self.velocity + self.acceleration(system, self.position)*deltaT
        if method == 'EC':  #Euler-Cromer Method
            self.velocity = self.velocity + self.acceleration(system, self.position)*deltaT
            self.position = self.position + self.velocity*deltaT    #Update position first using the final velocity
        if method == 'ER':  #Euler-Richardson Method
            xMid = self.position + 0.5*self.velocity*deltaT        #Calculates the position of the particle after time 0.5*deltaT with its initial velocity
            vMid = self.velocity + 0.5*self.acceleration(system, self.position)*deltaT    #Calculates the velocity of the particle after time 0.5*deltaT with its initial acceleration
            self.position = self.position + vMid*deltaT            #Updates position using velocity=vMid
            self.velocity = self.velocity + self.acceleration(system, xMid)*deltaT     #Updates velocity using the acceleration at position=xMid
            
    def kineticEnergy(self):
        """
        Returns the kinetic energy of the particle from its velocity array
        """
        velocitySquared = 0
        for component in self.velocity:     #Sums the square of each velocity component
            velocitySquared = velocitySquared + component**2
        return (0.5*self.mass*velocitySquared)
    
    def linearMomentum(self):
        """
        Returns the linear momentum vector of the particle as an array
        """
        return self.mass*self.velocity
    
    def angularMomentum(self):
        """
        Returns the angular momentum vector of the particle with respect to the origin (0,0,0) as an array
        """
        return np.cross(self.position,self.linearMomentum())
    
    def potentialEnergy(self, particleList):
        """
        Returns the gravitational potential energy of the particle with respect to the other particles in the system
        
        particleList = List of all the particle objects in the system
        """
        potential = 0
        for particle in particleList:
            if self != particle:    #No contribution from self
                positionVector = particle.position - self.position    #Vector from self to the other particle
                squareSum = 0
                for i in positionVector:    #Calculates the magnitude of positionVector dotted with itself
                    squareSum += i**2
                positionVectorAbs = np.sqrt(squareSum)      #Gives the magnitude of positionVector
                potential = potential + ((-scp.gravitational_constant)*self.mass*particle.mass/(positionVectorAbs))
        return potential
                
    initialPosition = np.array([0,0,0]) 
    initialVelocity = np.array([0,0,0])
    Name = 'Particle'
    mass = 1
    