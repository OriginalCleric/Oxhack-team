from inspect import currentframe
from Element import BaseElement

#image based

class BaseElementDecorator(BaseElement):
    wrapee = None
    def draw(self,timeElapsed):
        self.wrapee.draw()

class HoverableDecorator(BaseElementDecorator):
    pass

class ClickableDecorator(BaseElementDecorator):
    pass
