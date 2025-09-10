import pygame
import random
from enum import Enum

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
title_font = pygame.font.Font("Assets/DoodleJump.ttf", 60)
FPS = 60
BOUNCE = -1
GRAV = 0.981
START_JUMP_HEIGHT = 300

class GameStage(Enum):
  Menu = 1
  Play = 2
  Results = 3

Mode = GameStage.Menu

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

def add_text(text, x_pos, y_pos, font):
    added_text = font.render(text, True, (0,0,0))
    screen.blit(added_text, (x_pos, y_pos))

def Menu():
  screen.blit(background_image, (0, 0))
  add_text("doodle jump!", 90, 50, title_font)
  avatar.draw()
  avatar.update()
  avatar.MenuJump()
  MenuButtons()

def MenuButtons():
  PlayButton.draw()
  QuitButton.draw()
  if pygame.mouse.get_pressed()[0]:
      MousePos = pygame.mouse.get_pos()
      if PlayButton.IsPressed(MousePos):
        Mode = GameStage.Play
      if QuitButton.IsPressed(MousePos):
        running = False

PlayButton = buttons(pygame.transform.scale(pygame.image.load("Assets/play button image.png"), (250, 70)), screen_width/2 - 120, screen_height/2 - 205)
QuitButton = buttons(pygame.transform.scale(pygame.image.load("Assets/quit button image.png"), (250, 70)), screen_width/2 - 120, screen_height/2 - 100)

def mainloop():
  running = True
  while running ==  True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    match Mode:
      case GameStage.Menu:
        Menu()
      case GameStage.Play:
        Menu()
      case _:
        Menu()
    
    Clock.tick(FPS)
    pygame.display.update()
mainloop()
