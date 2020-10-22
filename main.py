import IOManager as io
import GameObjects as go
import time

stop = False
manette = io.InputManager()
score = 0

#Initializing game screen
gameBoundaries = [[5, 1] , [15, 11]]    #[[xleft,ytop] , [xright, ybottom]]
ecran = io.OutputManager(gameBoundaries)

#Initializing Snek
snakeStartingLength = 5
snakeStartingPoint = [abs(int((gameBoundaries[1][0]-gameBoundaries[0][0])/2)),\
                        abs(int((gameBoundaries[1][1]-gameBoundaries[0][1])/2))]  #Center of the screen.
snek = go.Snek(snakeStartingLength, snakeStartingPoint)

#Initializing Treat
treat = go.Treat(gameBoundaries, snek.position)


#Begining of the grand Master Loop !
while not stop :

    ecran.update(snek.position, treat.position, score)

    time.sleep(.3)  #Just after display so player has time to decide what to do.

    key_stroke = manette.getCurrentInput()

    if ecran.state == "game":
        #Updating game objects
        snek.update(key_stroke, gameBoundaries)
        treat.update(snek.position)
        if treat.dead:
            score += 1
            treat.reset(gameBoundaries, snek.position)
            snek.grow()

    elif ecran.state in ["startingScreen", "gameOver"] and key_stroke=="OK":
        #Begining a new game
        del snek, treat
        snek = go.Snek(snakeStartingLength, snakeStartingPoint)
        treat = go.Treat(gameBoundaries, snek.position)
        score = 0
        ecran.changeState("game")

    if snek.dead:
        ecran.changeState("gameOver")

    if key_stroke=='Stop':
        #Stop the loop
        stop=True