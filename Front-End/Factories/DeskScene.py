
from ..Scene import Scene

class DeskSceneFactory:
    def create():
        result = Scene()

        #background
        skyline = Element()
        background = Element()

        #decoration
        Decorations = CompositeElement()
        #TODO insert decorations here

        #desk
        desk = CompositeElement()
        deskBackground = Element()
        papers = Element()
        twitter = Element()
        controlPanel = Element()
        desk.add(papers)
        desk.add(twitter)
        desk.add(controlPanel)
        


