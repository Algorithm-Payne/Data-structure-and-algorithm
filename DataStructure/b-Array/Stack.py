class stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        self.item.pop()

    def length(self):
        return len(self.item)
