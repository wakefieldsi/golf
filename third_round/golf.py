from course import PebbleBeach
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
    return PebbleBeach()

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
