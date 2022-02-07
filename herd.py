from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.list = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('Ripper', 12)
        dino_two = Dinosaur('Rexalator', 12)
        dino_three = Dinosaur('Rocky', 12)

        self.list.append(dino_one)
        self.list.append(dino_two)
        self.list.append(dino_three)