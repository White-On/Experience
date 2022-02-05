import pygame
from Bot import Object

class Screen():
    image = pygame.image.load("Pygame/Background_2.png")
    def __init__(self,width = 700, height = 800):
        self.width = width
        self.height = height
        pygame.display.init()
        self.screen = pygame.display.set_mode([width,height],pygame.RESIZABLE,vsync=1)
        pygame.display.set_caption("Bot Trainning")
        self.load_background()
    
    def __repr__(self) -> str:
        return f"Screen(width = {self.width}, height = {self.height})"

    def changeSize(self,width:int,height:int):
        self.screen = pygame.display.set_mode([width,height],pygame.RESIZABLE,vsync=1)
        self.width = width
        self.height = height

    def afficher(self,object:Object):
        self.screen.blit(object.image,object.pos)
    
    def load_background(self):
        
        self.screen.blit(self.image, (0, 0))

