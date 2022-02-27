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


#discreet dragging
#not going to do continous, don't want to keep sending events
class SlidableDecorator(PressableDecorator):
    size = [0,0]
    values = [0,0]
    changed = False
    change = [0,0]
    mouseOriginal = [0,0]

    #there are 10 discreet steps in this slidable
    ranks = [10,10]
    steps = [0,0]

    #size indicates the maximum width and height that is slidable from the origin
    def __init__ (self,wrapee,rank,size):
        super(wrapee)
        self.rank = rank
        self.size = size
        self.steps = [(1/rank[0])*size[0],(1/rank[1])*size[1]]

    def press(self,mouse):
        self.pressed = True
        self.mouseOriginal = [mouse[0],mouse[1]]

    def unpress(self,mouse):
        self.pressed = False
        if (self.changed):
            self.Change()

    def Change(self):
        self.values = [self.values[0]+self.change[0],self.values[1]+self.change[1]]
        self.raiseEvent("CHANGEVALUE",self.values)

    def mouseDragged(self,mouse):
        if (self.pressed):
            self.change = self.getChange(mouse)
            if (self.change[0]!=0 or self.change[1]!=0):
                self.changed=True
            else:
                self.changed=False

    def getChange(self,mouse):
        #change in values
        change = [mouse[0]-self.mouseOriginal[0],mouse[1]-self.mouseOriginal[1]]
        stepChange = self.round(change)
        if (stepChange[0]+self.values[0]>self.ranks[0]):
            stepChange[0] = self.ranks[0]
        if (stepChange[1]+self.values[1]>self.ranks[1]):
            stepChange[1] = self.ranks[1]
        return stepChange

    #floor round values to the number of steps
    def round(self,values):
        return [values[0]//self.steps[0],values[1]//self.steps[1]]

        



