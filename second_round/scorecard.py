class Scorecard:
    def __init__(self):
        self.card = {}

    def score_hole(self, name, strokes):
        if name not in self.card:
            stroke_count = [strokes]
            self.card[name] = stroke_count
            print(self.card)
            return
        self.card[name].append(strokes)
        print(self.card)

    def final_score(self, strokes):
        return sum(strokes)

    def get_card(self):
        return self.card
