import pygame
import random

pygame.init()

screen_width = 400
screen_height = 700

AVATAR_WIDTH = 75
AVATAR_HEIGHT = 75

screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load("Assets/background.png")
background_image= pygame.transform.scale(background_image, (screen_width, screen_height))
rightavatar = pygame.image.load("Assets/avatarright.png")
rightavatar= pygame.transform.scale(rightavatar, (AVATAR_WIDTH, AVATAR_HEIGHT))
Clock = pygame.time.Clock()
FPS = 60
BOUNCE = -1
GRAV = 0.981
START_JUMP_HEIGHT = 300


class character():
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y
    self.xvel = 0
    self.yvel = 0

  def update(self):
    self.x += self.xvel
    self.y += self.yvel
  
  def MenuJump(self):
    if self.y > screen_height - AVATAR_HEIGHT:
      self.yvel *= BOUNCE
    else:
      self.yvel += GRAV

  def draw(self):
    screen.blit(self.image, (self.x, self.y))


class buttons():
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y
    self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

  def draw(self):
    screen.blit(self.image, (self.x, self.y))

  def IsPressed(self, MousePos)->bool:
    pressed = False
    if self.rect.collidepoint(MousePos):
      pressed = True
    return pressed


class block():
  def __init__(self, image, x, y):
    self.image = image


avatar = character(rightavatar, screen_width/2 - (AVATAR_WIDTH/2), screen_height-START_JUMP_HEIGHT)

def Menu():
  screen.blit(background_image, (0, 0)) 
  avatar.draw()
  avatar.update()
  avatar.MenuJump()
  MenuButtons()

def MenuButtons():
  # test
  PlayButton.draw()
  if pygame.mouse.get_pressed()[0]:
    MousePos = pygame.mouse.get_pos()
    if PlayButton.IsPressed(MousePos):
      print("Pressed")


PlayButton = buttons(pygame.transform.scale(pygame.image.load("Assets/blue empty button.jpeg"), (200, 50)), screen_width/2 - 150, screen_height/2 - 125)

def mainloop():
  running = True
  while running ==  True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    Menu()
    
    Clock.tick(FPS)
    pygame.display.update()
mainloop()
