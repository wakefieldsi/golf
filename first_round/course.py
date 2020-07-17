import random


def play_hole(hole):
    score = random.randint(hole.par - 2, hole.par + 2)
    return score


class Augusta:
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

    def first_hole(self):
        print(f"Welcome to hole number {self.first.get_number()} ")
        strokes = play_hole(self.first)
        print(f"You scored {strokes}")
        return strokes

    def second_hole(self):
        print(f"Welcome to hole number {self.second.get_number()} ")
        strokes = play_hole(self.second)
        print(f"You scored {strokes}")
        return strokes

    def third_hole(self):
        print(f"Welcome to hole number {self.third.get_number()} ")
        strokes = play_hole(self.third)
        print(f"You scored {strokes}")
        return strokes

    def fourth_hole(self):
        print(f"Welcome to hole number {self.fourth.get_number()} ")
        strokes = play_hole(self.fourth)
        print(f"You scored {strokes}")
        return strokes

    def fifth_hole(self):
        print(f"Welcome to hole number {self.fifth.get_number()} ")
        strokes = play_hole(self.fifth)
        print(f"You scored {strokes}")
        return strokes

    def sixth_hole(self):
        print(f"Welcome to hole number {self.sixth.get_number()} ")
        strokes = play_hole(self.sixth)
        print(f"You scored {strokes}")
        return strokes

    def seventh_hole(self):
        print(f"Welcome to hole number {self.seventh.get_number()} ")
        strokes = play_hole(self.seventh)
        print(f"You scored {strokes}")
        return strokes

    def eighth_hole(self):
        print(f"Welcome to hole number {self.eighth.get_number()} ")
        strokes = play_hole(self.eighth)
        print(f"You scored {strokes}")
        return strokes

    def ninth_hole(self):
        print(f"Welcome to hole number {self.ninth.get_number()} ")
        strokes = play_hole(self.ninth)
        print(f"You scored {strokes}")
        return strokes

    def tenth_hole(self):
        print(f"Welcome to hole number {self.tenth.get_number()} ")
        strokes = play_hole(self.tenth)
        print(f"You scored {strokes}")
        return strokes

    def eleventh_hole(self):
        print(f"Welcome to hole number {self.eleventh.get_number()} ")
        strokes = play_hole(self.eleventh)
        print(f"You scored {strokes}")
        return strokes

    def twelfth_hole(self):
        print(f"Welcome to hole number {self.twelfth.get_number()} ")
        strokes = play_hole(self.twelfth)
        print(f"You scored {strokes}")
        return strokes

    def thirteenth_hole(self):
        print(f"Welcome to hole number {self.thirteenth.get_number()} ")
        strokes = play_hole(self.thirteenth)
        print(f"You scored {strokes}")
        return strokes

    def fourteenth_hole(self):
        print(f"Welcome to hole number {self.fourteenth.get_number()} ")
        strokes = play_hole(self.eighth)
        print(f"You scored {strokes}")
        return strokes

    def fifteenth_hole(self):
        print(f"Welcome to hole number {self.fifteenth.get_number()} ")
        strokes = play_hole(self.fifteenth)
        print(f"You scored {strokes}")
        return strokes

    def sixteenth_hole(self):
        print(f"Welcome to hole number {self.sixteenth.get_number()} ")
        strokes = play_hole(self.sixteenth)
        print(f"You scored {strokes}")
        return strokes

    def seventeenth_hole(self):
        print(f"Welcome to hole number {self.seventeenth.get_number()} ")
        strokes = play_hole(self.seventeenth)
        print(f"You scored {strokes}")
        return strokes

    def eighteenth_hole(self):
        print(f"Welcome to hole number {self.eighteenth.get_number()} ")
        strokes = play_hole(self.eighteenth)
        print(f"You scored {strokes}")
        return strokes


