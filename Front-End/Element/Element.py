
from Main import draw


class BaseElement:
    backgroundColour = None
    borderColour = None
    scale = None
    offset = [0,0]
    visible = True
    origin = [0,0]

    #if this element is supposed to represent an object, this is the tag
    #use this to link the frontend and backend
    _Tag = None

    def draw(self,timeElapsed):
        pass

    def setOrigin(self,newOrigin):
        self.origin=newOrigin

    def getTag(self):
        return self._Tag
    
    def setTag(self,tag):
        self._Tag = tag
    
    def raiseEvent(self,eventName,eventArg):
        if (eventName in self.myEvents):
            callbacks = self.myEvents[eventName]
            for c in callbacks:
                c(eventArg)
    
    def subscribe(self,eventName,callback):
        if (eventName not in self.myEvents):
            self.myEvents[eventName] = []
        self.myEvents[eventName].append(callback)

    #calculates absolute position on canvas for rendering
    def getPosition(self):
        return [self.image,self.offset[0]+self.origin[0], self.offset[1]+self.origin[1]]
