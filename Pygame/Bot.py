import math
from turtle import speed, width
import pygame
import random

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
    def __init__(self, x = 50.0, y = 50.0,) -> None:
        super().__init__("Pygame/bot_droite_3.png",x,y)
        self.speed = 2
        self.rotation = 0
        self.cpt = 0
        self.rand = 1

        Bot.all.append(self)
    
    def __repr__(self) -> str:
        return f"Bot(x:{self.x}, y:{self.y})"
    
    def move(self):
        # Random Movement
        self.cpt = self.cpt +1
        if self.cpt == self.rand:
            self.rotation = (self.rotation + math.pi/2 * random.uniform(-math.pi,math.pi)) % (math.pi * 2)
            self.cpt = 0
            self.rand = random.randint(20,60)
        
        move_x = round(math.cos(self.rotation),2)*self.speed
        move_y = round(math.sin(self.rotation),2)*self.speed
        
        # Impossible movement
        if self.x + move_x <= 0 :
            move_x = - move_x
            self.rotation = self.rotation + math.pi
        elif self.x + move_x + self.pos.width > pygame.display.Info().current_w :
            move_x = - move_x
            self.rotation = self.rotation + math.pi
        elif self.y + move_y <= 0 :
            move_y = - move_y
            self.rotation = self.rotation + math.pi
        elif self.y + move_y + self.pos.height >= pygame.display.Info().current_h:
            move_y = - move_y
            self.rotation = self.rotation + math.pi

        # Changement de l'image du robot celon l'orientation
        if self.x + move_x >= self.x:
            self.image = Bot.img_droite

        else:
            self.image = Bot.img_gauche
        
        self.x = self.x + move_x
        self.y = self.y + move_y
        self.pos = self.image.get_rect().move(self.x,self.y)

    def draw_area(self):
        screen = pygame.display.get_surface()
        xr = self.x + self.pos.width/2
        yr = self.y + self.pos.height/2
        radius = self.pos.height*2
        pygame.draw.circle(screen,[255,255,255],[xr,yr],radius,width=1)

        
