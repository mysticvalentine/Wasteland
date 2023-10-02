from states.state import State
from states.gameWorld import GameWorld

class Title(State):
 def __init__(self, game):
  State.__init__(self, game)

 def update(self, deltaTime, actions):
  if actions["start"]:
   newState = GameWorld(self.game)
   newState.enterState()
  self.game.resetKeys()

 def render(self, display):
  display.fill((255,255,255))
  self.game.drawText(display, "Delta Rising", (0,0,0), self.game.gameWidth/2, self.game.gameHeight/2 )
