import random as rand
r = rand
class Special:
    def __init__(self, name, cost, damage, type):
        self.n = name
        self.c = cost
        self.dmg = damage
        self.t = type

    def _damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return r.randrange(low, high)

    