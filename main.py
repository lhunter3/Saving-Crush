import pygame, sys, time, random, colorsys, math
from pygame.math import Vector2
from pygame.locals import *
from button import Button



def main():
    pygame.init()

    #FPS
    clock = pygame.time.Clock()
    FPS = 60
    clock.tick(FPS)

    # set the display
    pygame.display.set_caption('Save the Turtles')
    DISPLAY=pygame.display.set_mode((640,480),0,32)


   
    
    
    # get fonts
    font_small = pygame.font.Font('data/fonts/font.otf', 32)

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

   
    
    menu = True

    while loadingScreenTimer < 100:

        
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        loadingScreenTimer += dt

        # drawing background and text
        DISPLAY.fill(DARKBLUE)
        startMessage = font_small.render("LOCATING TURTLES...", True, GREENBLUE)     
        DISPLAY.blit(startMessage, (DISPLAY.get_width()/2 - startMessage.get_width()/2, DISPLAY.get_height()/2 - startMessage.get_height()/2))

        # EXIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # update display
        pygame.display.update()



    while menu:

        # MENU BACKGROUND
        lsBg = pygame.image.load("data/gfx/lsBg2.jpeg")
        lsBg = pygame.transform.smoothscale(lsBg, (640,480))
        lsBgHeight = lsBg.get_height()
        lsBgWidth = lsBg.get_width()


        # TITLE 
        DISPLAY.blit(lsBg, (0,0))

        title = font_small.render("SAVE THE TURTLES",True, (0,0,0))
        DISPLAY.blit(title, (DISPLAY.get_width()/2 - title.get_width()/2, DISPLAY.get_height()/6 - title.get_height()/2))  

        ## MENU BUTTONS
        start_img = pygame.image.load("data/gfx/start_btn.png").convert()
        exit_img = pygame.image.load("data/gfx/exit_btn.png").convert()
        start_button = Button(DISPLAY.get_width()/4, 200, start_img, 0.4)
        exit_button = Button(DISPLAY.get_width()/2 , 200, exit_img, 0.4)
        
        ## START
        if start_button.draw(DISPLAY):
            print("START")
            menu = False
            game = True
            break

        ## EXIT
        if exit_button.draw(DISPLAY):
            pygame.quit()
            sys.exit()

        
        ## EXIT WINDOW
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # update display
        pygame.display.update()

        

    while game:

        #1. Scrolling bg
        #2. Loading Turtle Sprites.
        #3. Load Player
        #4. Turtle save 
        # UI

        DISPLAY.fill(WHITE)
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # update display
        pygame.display.update()




if __name__ == "__main__":
    main()
