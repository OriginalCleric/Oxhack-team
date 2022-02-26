#probably the object responsible for tieing the front and back together
#idk seems like a dima problem
class Game:
    currentScene = None
    allScenes = {}

    def changeScene(self,sceneName):
        self.currentScene = self.allScenes[sceneName]