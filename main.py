#import pygame
import os, time, sys, pygame
from states.title import Title
#import sys
#import Display
#import Character

class Game():
 def __init__(self):
  pygame.init()
  self.gameWidth, self.gameHeight = 480, 270
  self.screenWidth, self.screenHeight = 960, 540
  self.gameCanvas = pygame.Surface((self.gameWidth,self.gameHeight))
  self.screen = pygame.display.set_mode((self.screenWidth,self.screenHeight))
  self.running, self.playing = True, True
  self.actions = {"left": False,"right": False,"up": False,"down": False,"action1": False,"action2": False,"start": False}
  self.dt, self.prevTime = 0,0
  self.stateStack = []
  self.loadAssets()
  self.loadStates()

 def gameLoop(self):
  while self.playing:
   self.getDt()
   self.getEvents()
   self.update()
   self.render()

 def getEvents(self):
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    self.playing = False
    self.running = False
   elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_DOWN:
     self.actions["down"] = True
    elif event.key == pygame.K_UP:
     self.actions["up"] = True
    elif event.key == pygame.K_LEFT:
     self.actions["left"] = True
    elif event.key == pygame.K_RIGHT:
     self.actions["right"] = True
    elif event.key == pygame.K_p:
     self.actions["action1"] = True
    elif event.key == pygame.K_o:
     self.actions["action2"] = True
    elif event.key == pygame.K_RETURN:
     self.actions["start"] = True
    elif event.key == pygame.K_SPACE:
     self.actions["start"] = True
    elif event.key == pygame.K_ESCAPE:
     self.playing = False
     self.running = False

   if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT:
     self.actions['left'] = False
    if event.key == pygame.K_RIGHT:
     self.actions['right'] = False
    if event.key == pygame.K_UP:
     self.actions['up'] = False
    if event.key == pygame.K_DOWN:
     self.actions['down'] = False
    if event.key == pygame.K_p:
     self.actions['action1'] = False
    if event.key == pygame.K_o:
     self.actions['action2'] = False
    if event.key == pygame.K_RETURN:
     self.actions['start'] = False

 def update(self):
  self.stateStack[-1].update(self.dt,self.actions)

 def render(self):
  self.stateStack[-1].render(self.gameCanvas)
  self.screen.blit(pygame.transform.scale(self.gameCanvas,(self.screenWidth,self.screenHeight)), (0,0))
  pygame.display.flip()

 def getDt(self):
  now = time.time()
  self.dt = now - self.prevTime
  self.prevTime = now

 def drawText(self,surface,text,color,x,y):
  textSurface = self.font.render(text,True,color)
  textRect = textSurface.get_rect()
  textRect.center = (x,y)
  surface.blit(textSurface,textRect)

 def loadAssets(self):
  self.assetDir = os.path.join("assets")
  self.spriteDir = os.path.join(self.assetDir, "sprites")
  self.fontDir = os.path.join(self.assetDir, "font")
  self.font = pygame.font.Font(os.path.join(self.fontDir,"PressStart2P-vaV7.ttf"),20)

 def loadStates(self):
  self.titleScreen = Title(self)
  self.stateStack.append(self.titleScreen)

 def resetKeys(self):
  for action in self.actions:
   self.actions[action] = False

if __name__ == "__main__":
 g = Game()
 while g.running:
  g.gameLoop()
