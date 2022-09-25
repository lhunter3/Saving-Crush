from tkinter import font
import pygame, sys, time, random, colorsys, math
from pygame.math import Vector2
from pygame.locals import *
from button import Button
from shopButton import ShopButton
from turtle import Turtle
from player import Player
from util import Util

def main():
    pygame.init()

    #FPS
    clock = pygame.time.Clock()
    FPS = 60
    clock.tick(FPS)


    # gfx
    turtleA = "data/gfx/turtle.png"
    turtleB= "data/gfx/turtleB.png"

    shop = pygame.image.load('data/gfx/shop.png')
    shop_bg = pygame.image.load('data/gfx/shop_bg.png')

    # set the display
    pygame.display.set_caption('Save the Turtles')
    pygame.display.set_icon(Turtle(turtleA).sprite)
    DISPLAY=pygame.display.set_mode((640,480),0,32)
          
    # get fonts
    font_small = pygame.font.Font('data/fonts/font.otf', 32)
    big_font = pygame.font.Font('data/fonts/font.otf',64)
    font_smaller = pygame.font.Font('data/fonts/font.otf', 20)
    font = pygame.font.Font('data/fonts/font.otf', 100)

    # sfx   
    splash = pygame.mixer.Sound("data/sfx/splash.mp3")
    click = pygame.mixer.Sound("data/sfx/click.wav")
    hover = pygame.mixer.Sound("data/sfx/hover.wav")
    sploosh = pygame.mixer.Sound("data/sfx/sploosh.wav")
    underwater = pygame.mixer.Sound("data/sfx/underwater.wav")
    snip = pygame.mixer.Sound("data/sfx/snip.wav")
    death = pygame.mixer.Sound("data/sfx/death.wav")
    
    # COLORS
    BLUE=(29, 162, 216)
    WHITE=(222, 243, 246)
    GREENBLUE=(118, 182, 196)
    DARKBLUE=(6, 66, 115)
    BLACK = (0,0,0)

    # variables
    ssTimer = 0
    last_time = time.time()    
    menu = True
    player = Player()

    turtles = []
    turtleEnemies = []
    turtleMultiplier = 3
    turtleSpeed = 2
    buttons = []

   
    
    
    
    for i in range(turtleMultiplier): turtles.append(Turtle("data/gfx/turtle.png"))
    for turtle in turtles:
        turtle.position.xy = int(random.randrange(DISPLAY.get_width(), DISPLAY.get_width()+100)), random.randrange(0,DISPLAY.get_height()-turtle.sprite.get_height())

    sploosh.set_volume(0.5)
    sploosh.play()

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

    underwater.set_volume(0.2)
    underwater.play(5)
    

    while 1:

        sploosh.set_volume(0.3)
        sploosh.play()
        while menu:

            
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
            start_button = Button(100,300,"START",font_small,180,70)
            exit_button = Button(350,300,"QUIT",font_small,180,70)
            
            ## START
            if start_button.draw(DISPLAY):
                click.play()
                menu = False
                game = True
                break

            ## EXIT
            if exit_button.draw(DISPLAY):
                click.play()
                pygame.time.delay(100)
                pygame.quit()
                sys.exit()

            ## HIGH SCORE
            hs = font_smaller.render(str("Highscore: " + player.highscore),True, (30,30,30))
            DISPLAY.blit(hs, (DISPLAY.get_width() - 110, DISPLAY.get_height() - 40))
            ## EXIT WINDOW
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # update display
            
            pygame.display.update()
            pygame.time.delay(9)


        dead = False
        scroll = 0  
        cash = 0
        level = 0
        health = 100


        while game:

            health -= 0.1
            scroll -= 2

            """GAME BACKGROUND"""

            DISPLAY.fill(BLUE)
            bg = pygame.image.load("data/gfx/sea.png")
            tiles = math.ceil(DISPLAY.get_width()/ bg.get_width()) + 1
        
            for i in range(0, tiles):
                DISPLAY.blit(bg, (i * bg.get_width() + scroll, 0))

            
            if abs(scroll) >= bg.get_width():
                level += 1
                turtleSpeed += 1
                scroll = 0
  

            """SETTING UP ALL SPRITES"""

            # SETUP TURTLES SPRITES
            if turtles.__len__() < turtleMultiplier:

                for i in range(turtles.__len__(),turtleMultiplier):
                   temp = Turtle(turtleA)
                   temp.position.xy = int(random.randrange(DISPLAY.get_width(), DISPLAY.get_width()*2)), random.randrange(0,DISPLAY.get_height()-turtle.sprite.get_height())
                   turtles.append(temp)
          

            #SETUP TURTLE ENEMIES SPRITES
            if turtleEnemies.__len__() < math.ceil(turtleMultiplier/2):

                for i in range(turtleEnemies.__len__(),math.ceil(turtleMultiplier/2)):
                   temp = Turtle(turtleB)
                   temp.position.xy = int(random.randrange(DISPLAY.get_width(), DISPLAY.get_width()*2)), random.randrange(0,DISPLAY.get_height()-turtle.sprite.get_height())
                   turtleEnemies.append(temp)


            p = pygame.sprite.RenderPlain(player)

            """UPDATING STUFF"""

            # UPDATING TURTLES
            for turtle in turtles:
                #Remove if Off screen
                if turtle.update(turtleSpeed) == True:
                    turtles.remove(turtle)
                    
                  
            # UPDATING ENEMY TURTLES
            for turtle in turtleEnemies:
                #Remove if Off screen
                if turtle.update(turtleSpeed) == True:
                    turtleEnemies.remove(turtle)
                    health -=10

            p.update()

            if health >= 100:
                health = 100
            
            if health <= 0:
                game = False
                menu = False

                """ DEATH SCREEN!"""
                while 1:

                    if level > int(player.highscore) or player.highscore == "0":
                        with open("data/scores.txt", "w+",encoding="utf-8") as f:
                            player.highscore = level
                            f.write(str(player.highscore))
                        f.close()


                    title = font_small.render("TURTLES HAVE GONE EXTINCT!",True, (30,30,30))
                    DISPLAY.blit(title, (DISPLAY.get_width()/2 - title.get_width()/2, DISPLAY.get_height()/3 - title.get_height()/2))  

                    try_again = Button(100,300,"Try Again?",font_small,180,70)
                    quit = Button(350,300,"Exit",font_small,180,70)

                            ## START
                    if try_again.draw2(DISPLAY,hover):
                        click.play()
                        menu = False
                        health = 100
                        cash = 0
                        level = 0
                        game = True
                        
                        break

                    ## EXIT
                    if quit.draw2(DISPLAY,hover):
                        click.play()
                        pygame.time.delay(100)
                        pygame.quit()
                        sys.exit()
                    
                    # EXIT
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    
                    # update display
                    pygame.display.update()
                    
                    



            """DISPLAYING STUFF"""

             # LEVEL
            color = Util.hexcolor(level,[0,100],True)
            currentLevelMarker = font.render(str(level), True, (color))
            DISPLAY.blit(currentLevelMarker, (DISPLAY.get_width()/2 - currentLevelMarker.get_width()/2, DISPLAY.get_height()/2 - currentLevelMarker.get_height()))


            #TURTLE SPRITES   
            for turtle in turtles:
                DISPLAY.blit(turtle.sprite, (turtle.position.x,turtle.position.y + math.sin(time.time()*5)*2.5))

            #ENEMY TURTLE SPRITES    
            for turtle in turtleEnemies:
               DISPLAY.blit(turtle.sprite, (turtle.position.x , turtle.position.y + math.sin(time.time()*5)*2.5))

            #PLAYER
            #p.draw(DISPLAY)


           

            # CASH            
            DISPLAY.blit(font_small.render(str(cash).zfill(7), True, BLACK), (72, 394))


            # HEALTH BAR
            healthColor = Util.hexcolor(health,[0,100],False)
            pygame.draw.rect(DISPLAY,(healthColor),(21,437,150*(health/100),25))
            pygame.draw.rect(DISPLAY, BLACK, pygame.Rect(21, 437, 150, 25),  2)

            DISPLAY.blit(shop,(0,0))

            
            speed = Button(220,410,"speed",font_smaller,75,50)
            dunno = Button(330,410,"health",font_smaller,75,50)
            slowmow = Button(440,410,"slow-mo",font_smaller,75,50)
            
            
            
            ## START
            if speed.draw_game(DISPLAY):
                click.play()
            if dunno.draw_game(DISPLAY):
                click.play()
            if slowmow.draw_game(DISPLAY):
                click.play()
                
                

            """" 
            ## EXIT
            if exit_button.draw(DISPLAY):
                click.play()
                pygame.time.delay(100)
                pygame.quit()
                sys.exit()
            
            
            for button in buttons:
                button.draw(DISPLAY,220,393,)
                DISPLAY.blit(button.sprite, (220 + (buttons.index(button)*125), 393))
                priceDisplay = font_small.render(str(button.price), True, (0,0,0))
                DISPLAY.blit(priceDisplay, (262 + (buttons.index(button)*125), 408))
            """

            """EVENT LISTENNER"""

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for turtle in turtles:
                        if player.collision(turtle):
                            death.play()
                            turtles.remove(turtle)
                            health -= 10
                    for turtle in turtleEnemies:
                        if player.collision(turtle):
                            snip.play()
                            turtle.sprite = pygame.image.load("data/gfx/turtle.png")
                            turtles.append(turtle)
                            turtleEnemies.remove(turtle)
                            cash += 1
                            health += 15


                elif event.type == pygame.QUIT:
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
