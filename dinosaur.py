
class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
        self.energy = 50

    def attack(self, robot):
        robot.health -= self.attack_power

        print(f"{self.name} dealt {self.attack_power} damage to {robot.name}.")

        self.energy -= 10

        