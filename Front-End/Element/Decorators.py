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
    def mouseMoved(self,mouse):
        if (self.isInHitBox(mouse)):
            self.hover(mouse)

    def hover(self,mouse):
        #TODO
        self.wrapee.raiseEvent("HOVER")
        pass

    def isInHitBox(self,mouse):
        pos = self.wrapee.getPosition()   
        hitbox = self.wrapee.getHitbox()
        #TODO     
        return False

class ClickableDecorator(HoverableDecorator):
    hovered = False
    def hover(self):
        self.wrapee.raiseEvent("CLICKED")
        self.hover = True

    def mouseClicked(self,mouse):
        if (self.hovered):
            self.clicked(mouse)

    def clicked(self,mouse):
        self.wrapee.raiseEvent("CLICKED")
