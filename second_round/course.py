import random
from hole_decorator import HoleNumber

def play_hole(hole):
    score = random.randint(hole.par - 2, hole.par + 2)
    return score


class TroonNorth:
    def __init__(self, first, second=None, third=None, fourth=None, fifth=None, sixth=None, seventh=None, eighth=None,
                 ninth=None, tenth=None, eleventh=None, twelfth=None, thirteenth=None, fourteenth=None, fifteenth=None,
                 sixteenth=None, seventeenth=None, eighteenth=None):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        self.sixth = sixth
        self.seventh = seventh
        self.eighth = eighth
        self.ninth = ninth
        self.tenth = tenth
        self.eleventh = eleventh
        self.twelfth = twelfth
        self.thirteenth = thirteenth
        self.fourteenth = fourteenth
        self.fifteenth = fifteenth
        self.sixteenth = sixteenth
        self.seventeenth = seventeenth
        self.eighteenth = eighteenth

    @HoleNumber(1)
    def first_hole(self):
        strokes = play_hole(self.first)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(2)
    def second_hole(self):
        strokes = play_hole(self.second)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(3)
    def third_hole(self):
        strokes = play_hole(self.third)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(4)
    def fourth_hole(self):
        strokes = play_hole(self.fourth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(5)
    def fifth_hole(self):
        strokes = play_hole(self.fifth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(6)
    def sixth_hole(self):
        strokes = play_hole(self.sixth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(7)
    def seventh_hole(self):
        strokes = play_hole(self.seventh)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(8)
    def eighth_hole(self):
        strokes = play_hole(self.eighth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(9)
    def ninth_hole(self):
        strokes = play_hole(self.ninth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(10)
    def tenth_hole(self):
        strokes = play_hole(self.tenth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(11)
    def eleventh_hole(self):
        strokes = play_hole(self.eleventh)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(12)
    def twelfth_hole(self):
        strokes = play_hole(self.twelfth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(13)
    def thirteenth_hole(self):
        strokes = play_hole(self.thirteenth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(14)
    def fourteenth_hole(self):
        strokes = play_hole(self.eighth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(15)
    def fifteenth_hole(self):
        strokes = play_hole(self.fifteenth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(16)
    def sixteenth_hole(self):
        strokes = play_hole(self.sixteenth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(17)
    def seventeenth_hole(self):
        strokes = play_hole(self.seventeenth)
        print(f"You scored {strokes}")
        return strokes

    @HoleNumber(18)
    def eighteenth_hole(self):
        strokes = play_hole(self.eighteenth)
        print(f"You scored {strokes}")
        return strokes


