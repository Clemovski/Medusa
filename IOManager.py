import msvcrt   #For keyboard input
import time #For Timeout
import os   #For system('cls')

class InputManager:
    """Handles the keyboard inputs."""

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
        pass

    def getCurrentInput(self):
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
    """Handles display on screen."""

    def __init__(self):
        self.state = "startingScreen"

        self.topBoundary = 0
        self.bottomBoundary = 10
        self.leftBoundary = 0
        self.rightBoundary = 10

        self.largeur = abs(self.rightBoundary-self.leftBoundary)
        self.hauteur = abs(self.bottomBoundary-self.topBoundary)

    def withinBoundaries(self, x, y):
        return y>=self.topBoundary and y<self.bottomBoundary and x>=self.leftBoundary and x<self.rightBoundary

    def update(self, snakePos, treatPos, score):
        self.display(snakePos, treatPos, score)

    def changeState(self, newState):
        self.state=newState

    def display(self, snakePos, treatPos, score):
        #Clear console
        os.system('cls')

        if self.state == 'game':
            print((2*self.largeur+3)*'=')
    #Tester : Parcourir la liste avec un compteur et une fois trouvé le suivant, faire print(compteur*'\n') ou quoi ...
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
            print(f"\n{20*' '}GAME OVER")
            print(f"{20*' '}Score : {score}")
            print(f"\n{13*' '}Press Enter to start again.\n{18*' '}or Esc to quit.")


ecran = OutputManager()