from .brain import Brain

class Step:
    def __init__(self, name):
        self.name = name

    def __call__(self, brain: Brain):
        print(f"Running step: {self.name}")
