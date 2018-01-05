import random

class Worrior:
    inteligence = -1
    strenght = 100
    dexterity = 50

    def attack(self):
        print('called by {}'.format(self))
        return 'Worrior attack with strenght: '+str(random.sample(range(100),1))
