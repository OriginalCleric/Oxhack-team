#processing will call these to start our game

currentScene = None
allScenes = {}
game = None

#called to set up the canvas
#also TODO initialize the game object here
def setup():
    pass

#processing calls this to draw stuff
def draw():
    global game
    game.currentScene.draw()

#registers user inputs
def mousePressed():
    pass

def mouseMoved():
    pass