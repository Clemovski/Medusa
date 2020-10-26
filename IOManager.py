import msvcrt   #For keyboard input
import os   #For system('cls') to clear terminal
import random as rand   #For randomPosition

class InputManager:
    """Handles the keyboard inputs.
    
    keyCorrespondace : dict object. Gives the correspondance between the keypressed and its meaning.
    """

    keyCorrespondance = {
        'H':'u',
        'P':'d',
        'K':'l',
        'M':'r',
        'z':'u',
        's':'d',
        'q':'l',
        'd':'r',
        'Z':'u',
        'S':'d',
        'Q':'l',
        'D':'r',
        'r':'OK',
        'b':'Stop'
    }

    def ___init__(self):
        """Constructor."""
        pass

    def getCurrentInput(self):
        """Returns a character which is the meanging of the currently pressed key.
        
        'u' for up, 'd' for down, etc ...
        Stop and OK for Esc and Enter.
        """
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()

            #Flush buffer
            while msvcrt.kbhit():
                key_stroke = msvcrt.getch()

            if str(key_stroke)=="b'\\x00'":
                key_stroke = msvcrt.getch()
            
            key_stroke = str(key_stroke)[-2:-1]
            
            if key_stroke in self.keyCorrespondance:
                return self.keyCorrespondance[key_stroke]
        return None



class OutputManager:
    """Handles display on screen.
    
    state : String, tells if the manager should display the startingScreen, the game, or the game over screen.
    top/bottom/left/rightBoundary : Integers, position of the boundaries of the game board.
    largeur/hauteur : Integers, derivated from the boundaries.
    """

    def __init__(self, gameBoundaries):
        """Constructor.
        
        gameBoundaries : [[xleft,ytop] , [xright, ybottom]] coordinates of the game board.
        """

        self.state = "startingScreen"

        self.topBoundary = gameBoundaries[0][1]
        self.bottomBoundary = gameBoundaries[1][1]
        self.leftBoundary = gameBoundaries[0][0]
        self.rightBoundary = gameBoundaries[1][0]

        self.largeur = abs(self.rightBoundary-self.leftBoundary)
        self.hauteur = abs(self.bottomBoundary-self.topBoundary)

    def outOfBoundaries(self, x, y):
        """Checks if point (x;y) is out of gameBoundaries.

        x, y : int position of the game object within the game board.
        """

        return x<0 or x>=self.largeur\
            or y<0 or y>=self.hauteur

    def randomPosition(self):
        """Returns a random [x,y] within the game board.
        """
        randomX = int(self.largeur*rand.random())
        randomY = int(self.hauteur*rand.random())
        return [randomX, randomY]


    def changeState(self, newState):
        """Changes the state of the manager with newState.
        
        newState : String, within 'startingScreen', 'gameOver', 'game'
        """

        self.state=newState

    def update(self, snakePos, treatPos, score):
        """Displays the Screen according to the gameState and the different objects positions.
        
        snakePos : An array of [x,y] coordinates for each section of the snake.
        treatPos : [x,y] array for the position of the treat.
        score : Integer, player's score.
        """

        #Clear console
        os.system('cls')

        if self.state == 'game':
            #Display the game board and the game elements.
            leftPadding = 2*self.leftBoundary*" "
            print(self.topBoundary*'\n', end='')

            print(f"{leftPadding}{(2*self.largeur+3)*'='}")
            for line in range(self.hauteur):  #Pour chaque ligne de l'écran
                print(f"{leftPadding}|", end=' ')
                for x in range((self.largeur)):
                    if [x,line] in snakePos:
                        print("#", end=' ')
                    elif [x, line] == treatPos:
                        print("O", end=' ')
                    else:
                        print(" ", end=' ')
                print("|")

            print(f"{leftPadding}{(2*self.largeur+3)*'='}")

        elif self.state == "startingScreen":
            #Display the starting screen

            print("""
   ##  ##  ####    ####    ##  ##  ####-<  ####
   ######  #        # #    ##  ##  ##      #  #
   ##  ##  ####     # #    ##  ##   ##     ####
   ##  ##  #        # #    ##  ##    ##    #  #
   ##  ##  ####    ####    ######  ####    #  #

(A Snake game in Python with the help of Anaconda)
                
            Press Enter to begin
                Esc to quit
            """)

        elif self.state == "gameOver":
            #Display the game over screen

            print(2*'\n')
            print(f"{16*' '}GAME OVER")
            print(f"{16*' '}Score : {score}")
            print(f"\n{8*' '}Press Enter to start again.\n{13*' '}or Esc to quit.")
