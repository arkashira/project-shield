from .brain import Brain

class Chain:
    def __init__(self):
        self.brain = Brain()
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self):
        for step in self.steps:
            step(self.brain)
