class Brain:
    def __init__(self):
        self.knowledge = {}
        self.memory = {}
        self.datasets = {}
        self.context = {}
        self.product_portfolio = {}
        self.live_queue = []

    def add_knowledge(self, key, value):
        self.knowledge[key] = value

    def add_memory(self, key, value):
        self.memory[key] = value

    def add_dataset(self, key, value):
        self.datasets[key] = value

    def add_context(self, key, value):
        self.context[key] = value

    def add_product(self, key, value):
        self.product_portfolio[key] = value

    def add_to_queue(self, item):
        self.live_queue.append(item)
