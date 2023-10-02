import random

class Character:
 def __init__(self,name):
  self.name = name
  self.health = 1

 def setStats(self,attributes,proficiencies):
  self.attributes = attributes
  self.proficiencies = proficiencies
  self.hitpoints = (attributes["Endurance"] * 10)
  self.speed = (attributes["Agility"] * 10)

 def setArmor(self,armor):
  self.armor = armor

 def setWeapon(self,weapon):
  self.weapon = weapon

 def printStats(self):
  print(self.name)
  print("Hitpoints: ",self.hitpoints)
  print("Speed: ",self.speed)
  print("Armor: ",self.armor[0])
  print("Weapon: ",self.weapon[0])
  print()
  for x in self.attributes:
   print(x,": ",self.attributes[x])

#### Functions
def importCharacter(character):
 newChar = Character(character["Name"])
 newChar.setStats(character["Attributes"],character["Proficiencies"])
 newChar.setArmor(character["Armor"])
 newChar.setWeapon(character["Weapon"])
 return newChar

def genCharacter():
 f = open("names.txt","r")
 content = f.readlines()
 line = random.randint(1,len(content))
 f.close()
 name = content[line]
 return name

valentine = {
 "Name": "Valentine",
 "Attributes": {
                "Strength": 10,
                "Perception": 10,
                "Endurance": 10,
                "Charisma": 10,
                "Intelligence": 10,
                "Agility": 10,
                "Luck": 10,
               },
 "Armor": ("Leather",15,[]),
 "Weapon": ("Staff",5,[]),
 "Proficiencies": ["One-handed","Pistol"]
}

hixon = {
 "Name": "Hixon",
 "Attributes": {
                "Strength": 10,
                "Perception": 10,
                "Endurance": 10,
                "Charisma": 10,
                "Intelligence": 10,
                "Agility": 10,
                "Luck": 10,
               },
 "Armor": ("Riot",16,[]),
 "Weapon": ("M16",5,[]),
 "Proficiencies": ["Rifle","Pistol"]
}
