
class BaseElement:
    backgroundColour = None
    borderColour = None
    scale = None
    position = [0,0]
    visible = True

    #if this element is supposed to represent an object, this is the tag
    #use this to link the frontend and backend
    _Tag = None

    def draw(self,timeElapsed):
        pass

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


#made up of elements
class CompositeElement(BaseElement):
    Elements = []

    def draw(self,timeElapsed):
        if (self.visible):
            for e in self.Elements:
                e.draw(timeElapsed)
