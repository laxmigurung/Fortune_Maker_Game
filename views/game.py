class Game:
    def __init__(self, attempts):
        self.attempts = 10

    def attempts_track(self):
        self.attempts = self.attempts - 1
        return self.attempts
