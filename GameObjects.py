import random as rand   #For random treat position

class Snek:
    """The snake controlled by the player.
    
    position : An array of [x,y] coordinates representing each section of the snake.
    currentDirection : The direction the snake will go if no order is received.
    dead : True if the snake is dead, False else.
    growing : True if the snake should grow on its next call to move().
    """

    def __init__(self, initialLength, initialPos):
        """Constructor.
        
        initialLength : Interger, number of sections the snake has at the start.
        initialPos : [x,y] array, initial position of the snake's head.
        """
        
        self.position=[]
        for x in range(initialLength):
            self.position.append([initialPos[0]-x, initialPos[1]])
        self.currentDirection = 'r'
        self.dead = False
        self.growing = False

    def update(self, direction, gameBoundaries):
        """Updates the snake by making it move and checks its life state."""

        self.move(direction)
        self.checkState(gameBoundaries)

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
    
    def checkState(self, gameBoundaries):
        """Changes the snake's state to dead=True if it has encountered an obstacle or itself.
        
        gameBoundaries : [[xleft,ytop] , [xright, ybottom]] coordinates of the game board.
        """

        if self.position[0] in self.position[1:]:
            #If snake bites itself.
            self.dead = True

        if self.position[0][0]<gameBoundaries[0][0] or self.position[0][0]>=gameBoundaries[1][0]\
            or self.position[0][1]<gameBoundaries[0][1] or self.position[0][1]>=gameBoundaries[1][1]:
            #If snake is not within game boundaries.
            self.dead = True

    def grow(self):
        """Changes the snake's growing state to True. It will grow on next move or update."""

        self.growing = True




class Treat:
    """The treats appearing randomly on the game board.
    
    position : an array [x,y] giving the position of the treat.
    dead : boolean, indicates if the snake's head is on the treat.
    """

    def __init__(self, gameBoundaries, snakePosition):
        """Constructor.

        gameBoundaries : [[xleft,ytop] , [xright, ybottom]] coordinates of the game board.
        snakePosition: An array of [x,y] coordinates representing each section of the snake.
        """

        self.reset(gameBoundaries, snakePosition)
        self.dead = False
    
    def reset(self, gameBoundaries, snakePos):
        """Sets a new position for the treat.
        
        The new treat can't be on the snake.
        gameBoundaries : [[xleft,ytop] , [xright, ybottom]] coordinates of the game board.
        snakePosition: An array of [x,y] coordinates representing each section of the snake.
        """

        while True:
            randomX = abs(int((gameBoundaries[1][0] - gameBoundaries[0][0])*rand.random()) + gameBoundaries[0][0])
            randomY = abs(int((gameBoundaries[1][1] - gameBoundaries[0][1])*rand.random()) + gameBoundaries[0][1])
            self.position = [randomX, randomY]
            if self.position not in snakePos:
                break

    def update(self, snakePos):
        """Changes dead to True if the snake's head is on the treat. False else.
        
        snakePos : an array of [x,y] coordinates for each section of the snake.
        """

        if self.position == snakePos[0]:
            self.dead = True
        else:
            self.dead = False