class Hole:
    def __init__(self, yardage, number):
        self.yardage = yardage
        if yardage < 250:
            par = 3
        elif yardage < 470:
            par = 4
        elif yardage < 700:
            par = 5
        else:
            print("Hole is too long.")
            raise Exception
        self.par = par
        self.number = number

    def get_yardage(self):
        return self.yardage

    def get_par(self):
        return self.par

    def get_number(self):
        return self.number
