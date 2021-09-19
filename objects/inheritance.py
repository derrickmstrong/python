# Inheritance - Think of parent/child relationship

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, name):
        self.name = name
        print('Welcome,', self.name)
    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)

# FootballFan extends the PartyAnimal class
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        print(self.name, "scores", self.points, "points")
        self.party()

dan = FootballFan('Dan')
dan.party()
dan.touchdown()
dan.touchdown()
