#probably the object responsible for tieing the front and back together
#idk seems like a dima problem
class Game:
    currentScene = None
    allScenes = {}

    def changeScene(self,sceneName):
        self.currentScene = self.allScenes[sceneName]


#we may need the factory to be in the main folder instead?

#backend elements raise event in frontend elements
#eg. myLogicObject.itsFrontEndElement.raiseEvent("ChangeColour",eventArg)

#when attaching backend element to frontend element
#backend element can subscribe to frontend element's events
#eg. myLogicObject.itsFrontEndElement.subscribe("Clicked",callback)