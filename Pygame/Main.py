import pygame
import sys
import random
from Screen import *
from Bot import *


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

    for i in range(100):
        bot = Bot(350,400)

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
        
        screen.load_background()
        
        for b in Bot.all:
            b.move()
            #b.draw_area()
            screen.afficher(b)
            

        pygame.display.update()
        pygame.time.delay(10)

            

if __name__ == "__main__":
    main()