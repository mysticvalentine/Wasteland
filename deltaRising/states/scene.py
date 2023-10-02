class Scene():
 def __init__(self,scene,display):
#  self.game = game
  self.name = scene["name"]
  self.position = scene["position"]
  self.options = scene["options"]
  self.imageFile = scene["imageFile"]
#  self.image = pygame.image.load(os.path.join(self.game.assetDir, "map", x["imageFile"]))

 def getEvents(self):
  pass

 def update(self):
  pass

 def render(self):
  pass

