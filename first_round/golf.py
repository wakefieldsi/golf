from course import Augusta
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
    return Augusta(
        first=Hole(448, 1),
        second=Hole(578, 2),
        third=Hole(350, 3),
        fourth=Hole(241, 4),
        fifth=Hole(501, 5),
        sixth=Hole(187, 6),
        seventh=Hole(450, 7),
        eighth=Hole(570, 8),
        ninth=Hole(464, 9),
        tenth=Hole(492, 10),
        eleventh=Hole(505, 11),
        twelfth=Hole(155, 12),
        thirteenth=Hole(502, 13),
        fourteenth=Hole(442, 14),
        fifteenth=Hole(532, 15),
        sixteenth=Hole(170, 16),
        seventeenth=Hole(459, 17),
        eighteenth=Hole(462, 18)
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
