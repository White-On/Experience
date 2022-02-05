import pygame
import random

class Sommet():
    all = []
    def __init__(self, name: str, x: float, y: float) -> None:
        self.name = name
        self.x = x
        self.y = y
        Sommet.all.append(self)
    
    def __repr__(self) -> str:
        return f"Sommet(Nom : {self.name})"
    
    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.circle(screen,[14,209,69],[self.x,self.y],20)

class Arc():
    def __init__(self, s1 : Sommet, s2 : Sommet) -> None:
        self.s1 = s1
        self.s2 = s2
    
    def __repr__(self) -> str:
        return f"Arc(Sommet1 :{self.s1}, Sommet2: {self.s2})"

    def draw(self):
        screen = pygame.display.get_surface()
        pygame.draw.line(screen,[255,127,39],[self.s1.x,self.s1.y],[self.s2.x,self.s2.y],width=3)

class Graph():
    def __init__(self) -> None:
        self.sommets = []
        self.arcs = []
    
    def addSom(self,s:Sommet):
        self.sommets.append(s)
    
    def addAllSom(self,som):
        for s in som:
            self.sommets.append(s)
        
    def addArc(self,a:Arc):
        self.arcs.append(a)
    
    def addAllSom(self,arcs):
        for a in arcs:
            self.arcs.append(a)
    
    def draw(self):
        for arc in self.arcs:
            arc.draw()
        
        for sommet in self.sommets:
            sommet.draw()

    def generate(self):

        self.sommets = []
        self.arcs = []

        for i in range(10):
            s = Sommet(str(i), random.randint(50,pygame.display.Info().current_w - 50),random.randint(50,pygame.display.Info().current_h) - 50)
            self.addSom(s)
        
        for i in range(10):
            a = Arc(self.sommets[i],self.sommets[(i+1)%10])
            self.addArc(a)
    
    def sommetAcces(self,s : Sommet):
        sAcces = []

        for arc in self.arcs :
            if arc.s1 == s:
                sAcces.append(arc.s2)
            elif arc.s2 == s:
                sAcces.append(arc.s1)
        
        return sAcces

        