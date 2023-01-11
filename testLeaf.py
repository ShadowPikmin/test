#Create a Pikmin Class
class Pikmin:
  def __init__(self, type, stage, name):
    self.type = type
    self.stage = stage
    self.name = name 
   
  def getInfo(self):
    print("This is a " + self.type + " Pikmin named " + self.name  + " that is currently a " + self.stage + " pikmin")
    
    
pikmin = Pikmin("red", "leaf", "Steve")
pikmin.getInfo()
