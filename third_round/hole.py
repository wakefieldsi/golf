import random


def play_hole(par):
    score = random.randint(par - 2, par + 2)
    return score


class Hole:
    def __init__(self, hole_number, yardage):
        self.hole_number = hole_number
        self.yardage = yardage
        if yardage < 250:
            self.par = 3
        elif yardage < 470:
            self.par = 4
        else:
            self.par = 5

    def __call__(self, function):
        def wrapped(*args, **kwargs):
            print(f"Welcome to hole number {self.hole_number} with par {self.par} and {self.yardage} yards")
            strokes = play_hole(self.par)
            print(f"You scored {strokes}")
            if self.par == 3 and strokes == 1:
                print("Hole in 1! You win a car! Congratulations")
            if self.par-1 == strokes:
                print("You got a birdie!")
            if self.par != 3 and self.par - 2 == strokes:
                print("You got an eagle!")
            return strokes
        return wrapped
