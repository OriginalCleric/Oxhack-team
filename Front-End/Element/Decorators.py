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
    hovered = False
    def __init__ (self,wrapee):
        self.wrapee=wrapee
        #wrapee.subscribe()
    def mouseMoved(self,mouse):
        if (self.isInHitBox(mouse)):
            self.hover(mouse)
        else:
            self.unhover(mouse)

    def hover(self,mouse):
        self.hovered = True
        self.wrapee.raiseEvent("HOVER")

    def unhover(self,mouse):
        self.hovered = False
        self.wrapee.raiseEvent("UNHOVER")

    def isInHitBox(self,mouse):
        pos = self.wrapee.getPosition()   
        hitbox = self.wrapee.getHitbox()
        #TODO     
        return False

class PressableDecorator(HoverableDecorator):
    pressed = False

    def hover(self,mouse):
        self.hovered = True

    def unhover(self,mouse):
        self.hovered = False
        if (self.pressed):
            self.unpress(mouse)

    def mousePress(self,mouse):
        if (self.hovered):
            self.press(mouse)

    def mouseRelease(self,mouse):
        if (self.pressed):
            self.unpress(mouse)

    def press(self,mouse):
        self.pressed= True
        self.wrapee.raiseEvent("PRESSED")

    def unpress(self,mouse):
        self.pressed = False
        self.wrapee.raiseEvent("UNPRESSED")

#press and release in hitbox
class ClickableDecorator(PressableDecorator):

    def press(self,mouse):
        self.pressed = True

    def unpress(self,mouse):
        self.pressed = False
        if (self.hover):
            self.clicked(mouse)
        
    def clicked(self,mouse):
        self.wrapee.raiseEvent("CLICKED")


#dragging 
class SlidableDecorator(PressableDecorator):
    padding = [0,0]
    def clicked(self,mouse):
        pass

    def getMin(self):
        pass

    def getMax(self):
        pass

    def mouseDragged(self,mouse):
        pass

    def calculate(self,mouse):
        pos = self.getPosition()
        min = [self.padding[0]+pos[0],self.padding[1]+pos[1]]
        max = []
        range = [max[0]-min[0],max[1]-min[1]]
        mouseOriginal = []
        change = [mouse[0]-mouseOriginal[0],mouse[1]-mouseOriginal[1]]
        values = [mouse[0]-min[0],mouse[1]-min[1]]
        ratio = [values[0]/range[0],values[1]/range[1]]

