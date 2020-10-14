import IOManager as io  #To get informations from the screen
import random as rand   #For random treat position

class Snek:
    """The snake controlled by the player.
    
    position : An array of [x,y] coordinates representing each section of the snake.
    currentDirection : The direction the snake will go if no order is received.
    dead : True if the snake is dead, False else.
    growing : True if the snake should grow on its next call to move().
    """

    def __init__(self):
        """Constructor.
        
        Starting snake position is at the center of the screen.
        """

        initialLength = 5
        initialPos = [int(io.ecran.largeur/2) + io.ecran.leftBoundary - int(initialLength/2),\
                        int(io.ecran.hauteur/2) + io.ecran.topBoundary]
        
        self.position=[]
        for x in range(initialLength):
            self.position.append([initialPos[0]-x, initialPos[1]])
        self.currentDirection = 'r'
        self.dead = False
        self.growing = False

    def update(self, direction):
        """Updates the snake by making it move and checks its life state."""

        self.move(direction)
        self.checkState()

    def move(self, direction):
        """Updates the current position of the snake base on its direction.
        
        The direction is a character : 'u' for up, 'l' for left, etc ...
        The snake can't go in the direction opposite to its current one.
        The snake will grow if its growing state is True.
        """

        if direction not in ['u', 'd', 'l', 'r']\
            or (direction=='u' and self.currentDirection=='d')\
            or (direction=='d' and self.currentDirection=='u')\
            or (direction=='r' and self.currentDirection=='l')\
            or (direction=='l' and self.currentDirection=='r'):
            #Unauthorized direction
            direction=self.currentDirection
        else:
            #Good direction
            self.currentDirection=direction

        #Moving head
        newHead = [self.position[0][0] , self.position[0][1]]    #Ecriture dégueulasse pour éviter le passage par référence.
        if direction == 'u':
            newHead[1] -= 1
        elif direction == 'd':
            newHead[1] += 1
        elif direction == 'r':
            newHead[0] += 1
        elif direction == 'l':
            newHead[0] -= 1
        self.position.insert(0, newHead)

        #Deleting tail
        if(self.growing):
            self.growing = False
        else:
            self.position.pop(-1)

    
    def checkState(self):
        """Changes the snake's state to dead=True if it has encountered an obstacle or itself."""

        if self.position[0] in self.position[1:]:
            self.dead = True
        if not io.ecran.withinBoundaries(self.position[0][0], self.position[0][1]):
            self.dead = True

    def grow(self):
        """Changes the snake's growing state to True. It will grow on next move or update."""

        self.growing = True




class Treat:
    """The treats appearing randomly on the game board.
    
    position : an array [x,y] giving the position of the treat.
    """

    def __init__(self):
        """Constructor."""

        self.position = [io.ecran.leftBoundary + int((io.ecran.largeur)*rand.random()),\
                        io.ecran.topBoundary + int((io.ecran.hauteur)*rand.random())]
    
    def reset(self, snakePos):
        """Sets a new position for the treat.
        
        The new treat can't be on the snake."""

        while True:
            self.position = [io.ecran.leftBoundary + int((io.ecran.largeur)*rand.random()),\
                            io.ecran.topBoundary + int((io.ecran.hauteur)*rand.random())]
            if self.position not in snakePos:
                break

    def update(self, snakePos):
        """Returns 'dead' if the snake's head is on the treat. 'alive' else.
        
        snakePos : an array of [x,y] coordinates for each section of the snake."""

        if self.position == snakePos[0]:
            self.reset(snakePos)
            return 'dead'
        else:
            return 'alive'