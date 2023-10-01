import pygame, os
from states.state import State

class PartyMenu(State):
 def __init__(self, game):
  self.game = game
  State.__init__(self, game)

 def update(self, deltaTime, actions):
  if actions["action2"]:
   self.exitState()
  self.game.resetKeys()

 def render(self, display):
  display.fill((255,255,255))
  self.game.drawText(display, "PARTY MENU GOES HERE", (0,0,0), self.game.gameWidth/2, self.game.gameHeight/2 )

