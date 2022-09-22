import pygame, sys, time, random, colorsys, math
from pygame.math import Vector2
from pygame.locals import *
from button import Button
from turtle import Turtle



def main():
    pygame.init()

    #FPS
    clock = pygame.time.Clock()
    FPS = 60
    clock.tick(FPS)

    # set the display
    pygame.display.set_caption('Save the Turtles')
    pygame.display.set_icon(Turtle().sprite)
    DISPLAY=pygame.display.set_mode((640,480),0,32)
          
    # get fonts
    font_small = pygame.font.Font('data/fonts/font.otf', 32)

    # colors
    BLUE=(29, 162, 216)
    WHITE=(222, 243, 246)
    GREENBLUE=(118, 182, 196)
    DARKBLUE=(6, 66, 115)

    # variables

    ssTimer = 0
    last_time = time.time()    
    menu = True

    while ssTimer < 100:
   
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        ssTimer += dt

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
        start_button = Button(100,300,"START",font_small)
        exit_button = Button(350,300,"QUIT",font_small)
        
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

    scroll = 0  

    while game:

        #1. Scrolling bg
        #2. Loading Turtle Sprites.
        #3. Load Player
        #4. Turtle save 
        # UI

        # GAME BACKGROUND
        DISPLAY.fill(BLUE)
        bg = pygame.image.load("data/gfx/bg.jpg")
        tiles = math.ceil(DISPLAY.get_width()/ bg.get_width()) + 1
        scroll -= 1
        for i in range(0, tiles):
            DISPLAY.blit(bg, (i * bg.get_width() + scroll, 0))

        
        if abs(scroll) > bg.get_width():
            scroll = 0

   



        # Setup Turtle Sprites
        turtles = []
        for i in range(2): 
            turtles.append(Turtle())

        for turtle in turtles:
            turtle.position.xy = random.randrange(0, DISPLAY.get_width() - turtle.sprite.get_width()), random.randrange(0,DISPLAY.get_height()-turtle.sprite.get_height())

        camOffset = 0


        # Display Turtle Sprites
        for turtle in turtles:
            DISPLAY.blit(turtle.sprite, (turtle.position.x + camOffset, turtle.position.y))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # update display
        pygame.display.update()




if __name__ == "__main__":
    main()
