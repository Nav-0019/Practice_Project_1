class Game:
    def __init__(self, name):
        self.name = name
        self._score = 0

    @property
    def check_score(self):
        return f"{self.name} has {self._score} points."
    
    @check_score.setter
    def check_score(self, value):
        self._score = value

    def level_up(self):
        self._score += 1

        
gameA = Game("Shubham")
gameA.level_up()
gameA.level_up()
gameA.level_up()
print(gameA.check_score)