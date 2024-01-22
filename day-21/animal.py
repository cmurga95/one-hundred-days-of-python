class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()


nemo.breathe()

#The call to super() in the initialiser is recommended, but not strictly required.
