"""

"""
class Level:
    def __init__(self, level, points, attempts, prize_amount, total_hint):
        self.level = level
        self.points = points
        self.attempts = attempts
        self.prize_amount = prize_amount
        self.total_hint = total_hint

    def hint(self):
        self.total_hint = self.total_hint - 1
        return self.total_hint
