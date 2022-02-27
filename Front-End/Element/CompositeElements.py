from Element import BaseElement

#made up of elements
class CompositeElement(BaseElement):
    Elements = []

    def setOrigin(self,newOrigin):
        for e in self.Elements:
            e.setOrigin(self)

    def addElement(self,e):
        self.Elements.append(e)

    def getDecendent(self,childName):
        return None

    def draw(self,timeElapsed):
        if (self.visible):
            for e in self.Elements:
                e.draw(timeElapsed)

class GridElement(CompositeElement):
    rows = 0
    columns = 0
    gridVisibility = True

    def addElement(self,e):
        nextCellPosition = None
        newOrigin = self.calculateOrigin(nextCellPosition)
        e.origin = newOrigin
        super.addElement(e)

    def calculateOrigin(self,nextCell):
        offset = self.getCellOffset(nextCell)
        pos = self.getPosition()
        result = [pos[0]+offset[0],pos[1]+offset[1]]
        return result
    
    def draw(self,timeElapsed):
        if (self.gridVisibility):
            self.drawGrid()
            super.draw(self,timeElapsed)

    def drawGrid(self):
        #TODO
        pass
