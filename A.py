
import pygame, sys
from pygame.locals import QUIT

def collisions(): 
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
        rect.x = 0
        rect.y = 0
        rect2.x = 770
        rect2.y = 770
  
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
screen_width,screen_height = 800,800
pygame.display.set_caption('Shitty Tag Game!')
text_font = pygame.font.SysFont("Arial", 30)

rect = pygame.Rect(30,30,30,30)
rect2 = pygame.Rect(30,30,30,30)

#vars
rect.x = 0
rect.y = 0
rect2.x = 770
rect2.y = 770
black = (0, 0, 0)
player_speed = 8

while True:
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
    text = text_font.render("Hello, I am have you'r family",False,black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    screen.fill((255,255,255))
    screen.blit(text, (50,400))
    pygame.draw.rect(screen,pygame.Color('green'),rect)
    pygame.draw.rect(screen,pygame.Color('red'),rect2)
    collisions()
    pygame.display.update()
    clock.tick(60)