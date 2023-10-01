import pygame, os
from states.state import State
from states.pauseMenu import PauseMenu

class GameWorld(State):
 def __init__(self, game):
  State.__init__(self,game)
  self.player = Player(self.game)
  self.grassImg = pygame.image.load(os.path.join(self.game.assetDir, "map", "grass.png"))

 def update(self,deltaTime, actions):
  # Check if the game was paused
  if actions["start"]:
   newState = PauseMenu(self.game)
   newState.enterState()
  self.player.update(deltaTime, actions)

 def render(self, display):
  display.blit(self.grassImg, (0,0))
  self.player.render(display)

class Player():
 def __init__(self,game):
  self.game = game
  self.loadSprites()
  self.positionX, self.positionY = 200,200
  self.currentFrame, self.lastFrameUpdate = 0,0

 def update(self,deltaTime, actions):
  # Get the direction from inputs
  directionX = actions["right"] - actions["left"]
  directionY = actions["down"] - actions["up"]
  # Update the position
  self.positionX += 100 * deltaTime * directionX
  self.positionY += 100 * deltaTime * directionY
  # Animate the sprite
  self.animate(deltaTime,directionX,directionY)

 def render(self, display):
  display.blit(self.currImage, (self.positionX,self.positionY))

 def animate(self, deltaTime, directionX, directionY):
  # Compute how much time has passed since the frame last updated
  self.lastFrameUpdate += deltaTime
  # If no direction is pressed, set image to idle and return
  if not (directionX or directionY):
   self.currImage = self.currAnimList[0]
   return
  # If an image was pressed, use the appropriate list of frames according to direction
  if directionX:
   if directionX > 0: self.currAnimList = self.rightSprites
   else: self.currAnimList = self.leftSprites
  if directionY:
   if directionY > 0: self.currAnimList = self.frontSprites
   else: self.currAnimList = self.backSprites
        # Advance the animation if enough time has elapsed
  if self.lastFrameUpdate > .15:
   self.lastFrameUpdate = 0
   self.currentFrame = (self.currentFrame +1) % len(self.currAnimList)
   self.currImage = self.currAnimList[self.currentFrame]

 def loadSprites(self):
  # Get the diretory with the player sprites
  self.spriteDir = os.path.join(self.game.spriteDir, "player")
  self.frontSprites, self.backSprites, self.rightSprites, self.leftSprites = [],[],[],[]
  # Load in the frames for each direction
  for i in range(1,5):
   self.frontSprites.append(pygame.image.load(os.path.join(self.spriteDir, "player_front" + str(i) +".png")))
   self.backSprites.append(pygame.image.load(os.path.join(self.spriteDir, "player_back" + str(i) +".png")))
   self.rightSprites.append(pygame.image.load(os.path.join(self.spriteDir, "player_right" + str(i) +".png")))
   self.leftSprites.append(pygame.image.load(os.path.join(self.spriteDir, "player_left" + str(i) +".png")))
  # Set the default frames to facing front
  self.currImage = self.frontSprites[0]
  self.currAnimList = self.frontSprites
