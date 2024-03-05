"""
C88C Spring 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


# Car

class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)



# Quidditch

class QuidditchPlayer:
    def __init__(self, name, base_energy):
        """
        QuidditchPlayers have a name, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy

    def energy(self):
        return self.base_energy

class Beater(QuidditchPlayer):
    role = "bludgers"

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. 
        After playing for time minutes, Beaters lose their base energy level 
        divided by the number of minutes. If time is 0, catch the ZeroDivisionError 
        and print "You can't divide by zero!" instead.
        >>> fred = Beater("Fred Weasley", 640)
        >>> fred.energy(40)
        624.0
        >>> fred.energy(0)
        You can't divide by zero!
        """
        "*** YOUR CODE HERE ***"
        

class Chaser(QuidditchPlayer):
    role = "score"
    energy_expended = 20
    
    def __init__(self, name, base_energy, goals):
        """
        Chasers have a name, score goals, and begin with base_energy.
        """
        "*** YOUR CODE HERE ***"
        

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. For every goal 
        they score, they use energy_expended units of energy. In addition, they also use 
        10% of energy_expended if the number of minutes they have played is a multiple of 9.
        >>> katie = Chaser("Katie Bell", 230, 2)
        >>> katie.energy(20)
        190
        >>> ginny = Chaser("Ginny Weasley", 400, 3)
        >>> ginny.energy(45)
        338.0
        """
        "*** YOUR CODE HERE ***"
        

class Seeker(QuidditchPlayer):
    role = "snitch"
    energy_expended = 5

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. Seekers expend energy_expended 
        units of their energy for every minute they have been playing.
        >>> harry = Seeker("Harry Potter", 700)
        >>> harry.energy(30)
        550
        """
        "*** YOUR CODE HERE ***"
        

class Keeper(QuidditchPlayer):
    role = "guard"
    energy_expended = 50

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. If less than 30 minutes have 
        passed, then Keepers do not lose any energy. If 30 minutes or more have passed, 
        then Keepers expend 80% of their energy_expended units for every full 15 
        minutes that pass.
        >>> oliver = Keeper("Oliver Wood", 380)
        >>> oliver.energy(45)
        260.0
        """
        "*** YOUR CODE HERE ***"
        


