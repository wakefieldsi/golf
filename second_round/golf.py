from course import TroonNorth
from golfer import Golfer
from hole import Hole
from scorecard import Scorecard


def main():
    golfers = create_golfers()
    course = generate_course()
    scorecard = Scorecard()
    scorecard = play_round(golfers, scorecard, course)
    tally_score(scorecard)


def create_golfers():
    return [Golfer("Tiger Woods", 3),
            Golfer("Ernie Els", 7)]


def generate_course():
    return TroonNorth(
        first=Hole(448),
        second=Hole(578),
        third=Hole(350),
        fourth=Hole(241),
        fifth=Hole(501),
        sixth=Hole(187),
        seventh=Hole(450),
        eighth=Hole(570),
        ninth=Hole(464),
        tenth=Hole(492),
        eleventh=Hole(505),
        twelfth=Hole(155),
        thirteenth=Hole(502),
        fourteenth=Hole(442),
        fifteenth=Hole(532),
        sixteenth=Hole(170),
        seventeenth=Hole(459),
        eighteenth=Hole(462)
    )


def play_round(golfers, scorecard, course):

    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.first_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.second_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.third_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.fourth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.fifth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.sixth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.seventh_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.eighth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.ninth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.tenth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.eleventh_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.twelfth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.thirteenth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.fourteenth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.fifteenth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.sixteenth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.seventeenth_hole())
    for golfer in golfers:
        scorecard.score_hole(golfer.name, course.eighteenth_hole())
    return scorecard


def tally_score(scorecard):
    for name, strokes in scorecard.get_card().items():
        number_of_strokes = scorecard.final_score(strokes)
        print(f"{name} took {number_of_strokes} strokes to complete the course")


if __name__ == "__main__":
    main()
