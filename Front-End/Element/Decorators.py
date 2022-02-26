from inspect import currentframe
from Element import BaseElement

#image based

class BaseElementDecorator(BaseElement):
    #key is event name
    #value is a list containing all the call back functions
    myEvents = {}

    wrapee = None
    def draw(self,timeElapsed):
        self.wrapee.draw(timeElapsed)

    def getTag(self):
        return self.wrapee.getTag()
    
    def setTag(self,tag):
        self.wrapee.setTag(tag)

    def raiseEvent(self,eventName,eventArg):
        self.wrapee.raiseEvent(eventName,eventArg)
    
    def subscribe(self,eventName,callback):
        self.wrapee.subscribe(eventName,callback)

class HoverableDecorator(BaseElementDecorator):
    def __init__ (self,wrapee):
        self.wrapee=wrapee
        #wrapee.subscribe()
    
    def changeColour(self):
        pass

class ClickableDecorator(BaseElementDecorator):
    def activate(self):
        self.wrapee.raiseEvent("CLICKED")
