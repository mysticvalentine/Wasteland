import pygame, os
from states.state import State
from states.party import PartyMenu

class PauseMenu(State):
 def __init__(self, game):
  self.game = game
  State.__init__(self, game)
  # Set the menu
  self.menuImg = pygame.image.load(os.path.join(self.game.assetDir, "map", "menu.png"))
  self.menuRect = self.menuImg.get_rect()
  self.menuRect.center = (self.game.gameWidth*.85, self.game.gameHeight*.4)
  # Set the cursor and menu states
  self.menuOptions = {0 :"Party", 1 : "Items", 2 :"Magic", 3 : "Exit"}
  self.index = 0
  self.cursorImg = pygame.image.load(os.path.join(self.game.assetDir, "map", "cursor.png"))
  self.cursorRect = self.cursorImg.get_rect()
  self.cursorPosY = self.menuRect.y + 38
  self.cursorRect.x, self.cursorRect.y = self.menuRect.x + 10, self.cursorPosY

 def update(self, deltaTime, actions):
  self.updateCursor(actions)
  if actions["action1"]:
   self.transitionState()
  if actions["action2"]:
   self.exitState()
  self.game.resetKeys()

 def render(self, display):
  # render the gameworld behind the menu, which is right before the pause menu on the stack
  #self.game.state_stack[-2].render(display)
  self.prevState.render(display)
  display.blit(self.menuImg, self.menuRect)
  display.blit(self.cursorImg, self.cursorRect)

 def transitionState(self):
  if self.menuOptions[self.index] == "Party":
   newState = PartyMenu(self.game)
   newState.enterState()
  elif self.menuOptions[self.index] == "Items":
   pass # TO-DO
  elif self.menuOptions[self.index] == "Magic":
   pass # TO-DO
  elif self.menuOptions[self.index] == "Exit":
   while len(self.game.stateStack) > 1:
    self.game.stateStack.pop()

 def updateCursor(self, actions):
  if actions['down']:
   self.index = (self.index + 1) % len(self.menuOptions)
  elif actions['up']:
   self.index = (self.index - 1) % len(self.menuOptions)
  self.cursorRect.y = self.cursorPosY + (self.index * 32)

