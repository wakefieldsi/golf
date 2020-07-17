class HoleNumber:
    def __init__(self, hole_number):
        self.hole_number = hole_number

    def __call__(self, function):
        def wrapped(*args, **kwargs):
            print(f"Welcome to hole number {self.hole_number} ")
            return function(*args, **kwargs)
        return wrapped
