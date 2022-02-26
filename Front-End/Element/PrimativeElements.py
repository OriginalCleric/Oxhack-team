from Element import BaseElement

#draws image
class ImageElement(BaseElement):
    imageName = ""
    image = None

    def load(self,imageName):
        self.image = loadImage(imageName)

    def draw(self,timeElapsed):
        if (self.visible):
            image(self.image,self.position[0],self.position[1])

    #transform the current element
    def update():
        pass

#draws squares
class SquareElement(BaseElement):
    size = [10,10]

    def draw(self,timeElapsed):
        if (self.visible):
            fill(self.backgroundColour)
            square(self.position[0], self.position[1], self.size[0])

class TextElement(BaseElement):
    size = [10,10]
    fontsize = 10

    def draw(self,timeElapsed):
        pass


#animes stuff
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