import IOManager as io
import random as rand   #For random treat position

class Snek:
    def __init__(self):
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
        self.move(direction)
        self.checkState()

    def move(self, direction):
        
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
        if self.position[0] in self.position[1:]:
            self.dead = True
        if not io.ecran.withinBoundaries(self.position[0][0], self.position[0][1]):
            self.dead = True

    def grow(self):
        self.growing = True




class Treat:

    def __init__(self):
        self.position = [io.ecran.leftBoundary + int((io.ecran.largeur)*rand.random()),\
                        io.ecran.topBoundary + int((io.ecran.hauteur)*rand.random())]
    
    def reset(self, snakePos):
        while True:
            self.position = [io.ecran.leftBoundary + int((io.ecran.largeur)*rand.random()),\
                            io.ecran.topBoundary + int((io.ecran.hauteur)*rand.random())]
            if self.position not in snakePos:
                break

    def update(self, snakePos):
        if self.position == snakePos[0]:
            self.reset(snakePos)
            return 'dead'
        else:
            return 'alive'