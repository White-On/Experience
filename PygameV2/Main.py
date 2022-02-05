import pygame
import sys
import random
from Screen import *
from Bot import *
from Graph import *


# white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (105, 105, 105)
pink = (255, 182, 193)
purple = (128, 0, 128)
sky_blue = (135, 206, 250)
e_colour = (51, 51, 51)
back_col = (255, 255, 0)
above_col = (248, 255, 255)
white = above_col


def main():
    global screen, clock
    pygame.init()

    screen = Screen()

    #Graph Init
    graph = Graph()
    graph.generate()



    #Bot Init
    for i in range(1):
        bot = Bot(graph)
    

    clock = pygame.time.Clock()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen.changeSize(event.w,event.h)
                screen.load_background()
            if event.type == pygame.MOUSEBUTTONDOWN:
                graph.generate()
        
        screen.load_background()
        graph.draw()
        
        for b in Bot.all:
            b.move(graph.sommetAcces(b.sommet))
            #b.draw_area()
            screen.afficher(b)
        
            

        pygame.display.update()
        pygame.time.delay(10)

            

if __name__ == "__main__":
    main()