"""Definit les classe d'outils"""

class ToolBox:
    """boite à outils"""

    def __init__(self):
        """initialise les outils"""
        self.tools=[]
    
    def add_tool(self,tool):
        """ajoute un outil"""
        pass 

    def remove_tool(self,tool):
        """enleve un outil"""
        pass 

class Tournevis: 
    def __init__(self,size):
        """Initialise la taille."""
        self.size = size

    def tighten(self,screw):
        """serrer une vis"""
        pass 

    def loosen(self,screw):
        """desserre une vis"""
        pass 

class Hammer: 
    """Marteau"""
    def __init__(self,color) :
        """initialise la couleur"""
        self.color=color

    def paint(self,color):
        """paint le marteau"""
        pass 

    def hammer_in(self,nail):
        """enfonce le marteau"""
        pass

    def remove(self,nail):
        """enleve un clou"""
        pass

