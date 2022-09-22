import pygame, sys, time, random, colorsys, math
from pygame.math import Vector2
from pygame.locals import *
from background import Background


def main():
    pygame.init()


    #FPS
    clock = pygame.time.Clock()
    FPS = 60

    # set the display
    DISPLAY=pygame.display.set_mode((640,480),0,32)
    pygame.display.set_caption('Save the Turtles')
    lsBg = pygame.image.load("data/gfx/lsBg.png").convert()
    lsBgHeight = lsBg.get_height()
    lsBgWidth = lsBg.get_width()
    lsBgRec = lsBg.get_rect()
    
    tiles = math.ceil(480/lsBgHeight) +1
    
    
    # get fonts
    font_small = pygame.font.Font('data/fonts/font.otf', 32)

    # get some images
    

    # get sounds
    


    # colors
    BLUE=(29, 162, 216)
    WHITE=(222, 243, 246)
    GREENBLUE=(118, 182, 196)
    DARKBLUE=(6, 66, 115)

    # variables

    loadingScreenTimer = 0
    last_time = time.time()
    loadingScreenScroll = 0
    loadingScreenScrollX = 0
    # creating a new object player

   

    

    while loadingScreenTimer < 100:

        clock.tick(FPS)
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        loadingScreenTimer += dt

        startMessage = font_small.render("LOCATING TURTLES", True, WHITE)
        

        # loadingScreen background
        for i in range(0, tiles):
            DISPLAY.blit(lsBg, (0.2*loadingScreenScrollX,i * lsBgHeight + loadingScreenScroll))

        loadingScreenScroll -= 3
        loadingScreenScrollX += 3
                        
        #reset scroll
        if abs(loadingScreenScroll) > lsBgHeight:
            loadingScreenScroll = 0
    
        if abs(loadingScreenScrollX) > lsBgWidth:
            loadingScreenScrollX = 0

        # loadingScreen text
        DISPLAY.blit(startMessage, (DISPLAY.get_width()/2 - startMessage.get_width()/2, DISPLAY.get_height()/2 - startMessage.get_height()/2))

        # EXIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # update display
        pygame.display.update()




        




if __name__ == "__main__":
    main()
