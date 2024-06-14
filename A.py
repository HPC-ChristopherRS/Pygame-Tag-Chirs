import pygame, sys
from pygame.locals import QUIT
import random

#The timer, if it reaches 0 the game closes and prints the winner
def timer():
    global counter, run, it
    if counter <= 0:
        run = False
        print("You win player " + str(it))

#Checks to see if the players collide, if so their positions reset. If touching the walls, 0 - 800, the player is pushed out at the same speed it is moving when colliding with it. It also draws the text for the player it, by putting the int(it) in a string.
def collisions():
    global it
    if rect.right >= 800:
        rect.x -= player_speed
    if rect.bottom >= 800:
        rect.y -= player_speed
    if rect.right <= 30:
        rect.x += player_speed
    if rect.bottom <= 30:
        rect.y += player_speed    
    if rect2.right >= 800:
        rect2.x -= player_speed
    if rect2.bottom >= 800:
        rect2.y -= player_speed
    if rect2.right <= 30:
        rect2.x += player_speed
    if rect2.bottom <= 30:
        rect2.y += player_speed
       
    if rect.colliderect(rect2):
        if it == 1:
            it = 2
        elif it == 2:
            it = 1
           
        rect.x = 0
        rect.y = 0
        rect2.x = 770
        rect2.y = 770
       
    text1=my_font.render("Player "+str(it)+" is it",40,black)
    text2=my_font.render("Time: "+str(int(counter)),40,black)
    screen.blit(text1,(350,10))
    screen.blit(text2,(630,10))

#Draws the window, and sets a user event for the timer, also sets up fonts and sets the background. 
pygame.init()
pygame.display.set_caption('Shitty Tag Game!')
my_font=pygame.font.SysFont("Arial", 40)
screen = pygame.display.set_mode((800, 800))
screen_width,screen_height = 800,800
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 800)
bg_surface = pygame.image.load('images.png').convert()
bg_surface = pygame.transform.scale_by(bg_surface,(4,4))

rect = pygame.Rect(30,30,30,30)
rect2 = pygame.Rect(30,30,30,30)

#vars, startiing pos, speed, colors, and timer. 
rect.x = 0
rect.y = 0
rect2.x = 770
rect2.y = 770
black = (0, 0, 0)
player_speed = 7
black=(0,0,0)
it = random.randint(1,2)
counter = 60

#game code, for movement, moves rects depending on playerspeed, and also blits the rects and functions. 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        rect.x += player_speed
    if keys[pygame.K_a]:
        rect.x -= player_speed
    if keys[pygame.K_s]:
        rect.y += player_speed
    if keys[pygame.K_w]:
        rect.y -= player_speed
    if keys[pygame.K_RIGHT]:
        rect2.x += player_speed
    if keys[pygame.K_LEFT]:
        rect2.x -= player_speed
    if keys[pygame.K_DOWN]:
        rect2.y += player_speed
    if keys[pygame.K_UP]:
        rect2.y -= player_speed
   
    screen.blit(bg_surface, (0,0))
    pygame.draw.rect(screen,pygame.Color('green'),rect)
    pygame.draw.rect(screen,pygame.Color('red'),rect2)
    collisions()
    timer()
    pygame.display.update()
    clock.tick(60)
