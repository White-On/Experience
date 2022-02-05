import math
from turtle import speed, width
import pygame
import random
from Graph import *

class Object():
    def __init__(self,image ,x = 50.0, y = 50.0) -> None:
        self.x = x 
        self.y = y 
        self.image = pygame.image.load(image)
        self.pos = self.image.get_rect().move(x,y)
        

class Bot(Object):
    all = []
    img_droite = pygame.image.load("Pygame/bot_droite_3.png")
    img_gauche = pygame.image.load("Pygame/bot_gauche_3.png")
    def __init__(self,graph : Graph, x = 50.0, y = 50.0) -> None:
        self.sommet = graph.sommets[random.randint(0,len(graph.sommets)-1)]
        super().__init__("Pygame/bot_droite_3.png",self.sommet.x,self.sommet.y)
        self.speed = 2
        self.rotation = 0
        self.cpt = 0
        self.rand = 1

        Bot.all.append(self)
    
    def __repr__(self) -> str:
        return f"Bot(x:{self.x}, y:{self.y},sommet:{self.sommet})"
    
    def move(self,sAcces):
        sDir = sAcces[random.randint(0,len(sAcces)-1)]
        self.x = sDir.x
        self.y = sDir.y
        self.sommet = sDir
        self.pos = self.image.get_rect().move(self.x,self.y)

    def draw_area(self):
        screen = pygame.display.get_surface()
        xr = self.x + self.pos.width/2
        yr = self.y + self.pos.height/2
        radius = self.pos.height*2
        pygame.draw.circle(screen,[255,255,255],[xr,yr],radius,width=1)

        
