import msvcrt   #For keyboard input
import time #For Timeout
import os   #For system('cls')

class InputManager:
    """Handles the keyboard inputs.
    
    keyCorrespondace : dict object. Gives the correspondance between the keypressed and its meaning.
    """

    keyCorrespondance = {   #
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
    
    state : Tells if the manager should display the startingScreen, the game, or the game over screen.
    top/bottom/left/rightBoundary : Position of the boundaries of the game board.
    largeur/hauteur : derivated from the boundaries.
    """

    def __init__(self):
        """Constructor."""

        self.state = "startingScreen"

        self.topBoundary = 0
        self.bottomBoundary = 10
        self.leftBoundary = 0
        self.rightBoundary = 10

        self.largeur = abs(self.rightBoundary-self.leftBoundary)
        self.hauteur = abs(self.bottomBoundary-self.topBoundary)

    def withinBoundaries(self, x, y):
        """Returns True if [x, y] is within the frame's boundaries. False else."""

        return y>=self.topBoundary and y<self.bottomBoundary and x>=self.leftBoundary and x<self.rightBoundary

    def changeState(self, newState):
        """Changes the state of the manager with newState."""

        self.state=newState

    def update(self, snakePos, treatPos, score):
        """Displays the Screen according to the gameState and the different objects positions.
        
        snakePos : An array of [x,y] coordinates for each section of the snake.
        treatPos : [x,y] array for the position of the treat.
        score : Player's score.
        """

        #Clear console
        os.system('cls')

        if self.state == 'game':
            #Display the game board and the game elements.

            print((2*self.largeur+3)*'=')
            for line in range((self.hauteur)):  #Pour chaque ligne de l'écran
                print("|", end=' ')
                for x in range((self.largeur)):
                    if [x,line] in snakePos:
                        print("#", end=' ')
                    elif [x, line] == treatPos:
                        print("O", end=' ')
                    else:
                        print(" ", end=' ')
                print("|")

            print((2*self.largeur+3)*'=')

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
            
            print(f"\n{20*' '}GAME OVER")
            print(f"{20*' '}Score : {score}")
            print(f"\n{13*' '}Press Enter to start again.\n{18*' '}or Esc to quit.")


ecran = OutputManager()