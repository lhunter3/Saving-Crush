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
    big_font = pygame.font.Font('data/fonts/font.otf',64)

    # sfx   
    splash = pygame.mixer.Sound("data/sfx/splash.mp3")
    click = pygame.mixer.Sound("data/sfx/click.wav")
    hover = pygame.mixer.Sound("data/sfx/hover.wav")
    # COLORS
    BLUE=(29, 162, 216)
    WHITE=(222, 243, 246)
    GREENBLUE=(118, 182, 196)
    DARKBLUE=(6, 66, 115)

    # variables
    ssTimer = 0
    last_time = time.time()    
    menu = True


    turtles = []
    turtleMultiplier = 2

    for i in range(turtleMultiplier): turtles.append(Turtle())
    for turtle in turtles:
        turtle.position.xy = random.randrange(0, DISPLAY.get_width() - turtle.sprite.get_width()), random.randrange(0,DISPLAY.get_height()-turtle.sprite.get_height())

    while ssTimer < 75:
   

        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        ssTimer += dt

        # drawing background and text
        DISPLAY.fill(DARKBLUE)
        startMessage = font_small.render("LOCATING TURTLES...", True, GREENBLUE)     
        DISPLAY.blit(startMessage, (DISPLAY.get_width()/2 - startMessage.get_width()/2, DISPLAY.get_height()/2 - startMessage.get_height()/2))

        splash.set_volume(0.05)
        splash.play()

        # EXIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # update display
        pygame.display.update()

    while 1:


        while menu:

            splash.fadeout(0)
            click.set_volume(1)
            
            # MENU BACKGROUND
            lsBg = pygame.image.load("data/gfx/lsBg2.jpeg")
            lsBg = pygame.transform.smoothscale(lsBg, (640,480))
            lsBgHeight = lsBg.get_height()
            lsBgWidth = lsBg.get_width()


            # TITLE 
            DISPLAY.blit(lsBg, (0,0))

            title = big_font.render("SAVE THE TURTLES",True, (30,30,30))
            DISPLAY.blit(title, (DISPLAY.get_width()/2 - title.get_width()/2, DISPLAY.get_height()/3 - title.get_height()/2 + math.sin(time.time()*5)*2.5 - 25))  

            ## MENU BUTTONS
            start_button = Button(100,300,"START",font_small)
            exit_button = Button(350,300,"QUIT",font_small)
            
            ## START
            if start_button.draw(DISPLAY,hover):
                click.play()
                menu = False
                game = True
                break

            ## EXIT
            if exit_button.draw(DISPLAY,hover):
                click.play()
                pygame.time.delay(100)
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
        dead = False
        camOffset = 0

        while game:

            dt = time.time() - last_time
            dt *= 60
            last_time = time.time()
            mouseX,mouseY = pygame.mouse.get_pos()
            #1. Scrolling bg
            #2. Loading Turtle Sprites.
            #3. Load Player
                # player follows mouse
                # check for collision on click
                
            #4. Turtle save 
            # UI

            # GAME BACKGROUND
            DISPLAY.fill(BLUE)
            bg = pygame.image.load("data/gfx/sea.png")
            tiles = math.ceil(DISPLAY.get_width()/ bg.get_width()) + 1
            scroll -= 1
            for i in range(0, tiles):
                DISPLAY.blit(bg, (i * bg.get_width() + scroll, 0))

            
            if abs(scroll) > bg.get_width():
                scroll = 0
  



            # SETUP TURTLEs SPRITES
            if turtles.__len__() < turtleMultiplier:

                for i in range(turtles.__len__(),turtleMultiplier):
                   turtles.append(Turtle())
                
                for turtle in turtles:
                        turtle.position.xy = random.randrange(0, DISPLAY.get_width() - turtle.sprite.get_width()), random.randrange(0,DISPLAY.get_height()-turtle.sprite.get_height())

            for turtle in turtles:
                DISPLAY.blit(turtle.sprite, (turtle.position.x , turtle.position.y))
                    

        

            # DISPLAY TURTLE SPRITES
           # for turtle in turtles:
           #     DISPLAY.blit(turtle.sprite, (turtle.position.x + camOffset, turtle.position.y))

            for turtle in turtles:
                if turtle.update() == True:
                    turtles.remove(turtle)

    
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # update display
            pygame.display.update()
            pygame.time.delay(10)

            if dead == True:
                menu = True
                break




if __name__ == "__main__":
    main()
