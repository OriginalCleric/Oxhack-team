#abstract
class BaseElement:
    backgroundColour = None
    borderColour = None
    scale = None
    position = [0,0]

    def draw(self,timeElapsed):
        pass

class CompositeElement(BaseElement):
    Elements = []

    def draw(self,timeElapsed):
        for e in self.Elements:
            e.draw(timeElapsed)

#render text, image and geomatry
class StaticElement(BaseElement):
    def draw(self,timeElapsed):
        pass

class ImageElement(BaseElement):
    imageName = ""
    image = None

    def load(self,imageName):
        self.image = loadImage(imageName)

    def draw(self,timeElapsed):
        image(self.image,self.position[0],self.position[1])

    #transform the current element
    def update():
        pass

class SquareElement(BaseElement):
    size = [10,10]

    def draw(self,timeElapsed):
        fill(self.backgroundColour)
        square(self.position[0], self.position[1], self.size[0])

class AnimatedElement(BaseElement):
    FPS = 2
    currentFrameIndex = 0
    #ideally a list of static elements
    allFrames = []
    
    def draw(self,timeElapsed):
        #animate
        newIndex = self.currentframeIndex+self.getFrameChange(timeElapsed)
        self.updateFrame(newIndex)
        self.allFrames[self.currentFrameIndex].draw()
        super.draw()

    def updateFrame(self,newIndex):
        currentFrameIndex=newIndex

    def getFrameChange(self,timeElapsed):
        return timeElapsed//self.FPS