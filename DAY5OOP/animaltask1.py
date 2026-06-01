class animal:
    def __init__(self,name,sound):
        self.name= name
        self.sound= sound
    def speak(self):
       print( self.speak )
class dog(animal):
    def speak(self):
        print(f"{self.name} says {self.sound}")
class cat(animal):
    def speak(self):
        print(f"{self.name} says {self.sound}")       
d1 = dog("berry","bow bow")
c1 = cat("cozy","meow meow")
d1.speak()
c1.speak()
