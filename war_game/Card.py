class Card:
    def __init__(self, name, value, color):
        self.name = name
        self.value = value
        self.color = color

    def __str__(self):
        return f'{self.name, self.color}'