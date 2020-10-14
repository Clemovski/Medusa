import IOManager as io
import GameObjects as go
import time

stop = False
manette = io.InputManager()
snek = go.Snek()
treat = go.Treat()
score = 0

while not stop :

    io.ecran.update(snek.position, treat.position, score)

    time.sleep(.3)  #Just after display so player has time to decide what to do.

    key_stroke = manette.getCurrentInput()

    if io.ecran.state == "game":
        #Updating game objects
        snek.update(key_stroke)
        if(treat.update(snek.position)=='dead'):
            score += 1
            snek.grow()

    elif io.ecran.state in ["startingScreen", "gameOver"] and key_stroke=="OK":
        #Begining a new game
        io.ecran.changeState("game")
        score = 0

    if snek.dead==True:
        io.ecran.changeState("gameOver")
        del snek, treat
        snek = go.Snek()
        treat = go.Treat()

    if key_stroke=='Stop':
        #Stop the loop
        stop=True