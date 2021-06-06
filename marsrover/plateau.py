from dataclasses import dataclass

@dataclass
class Plateau:
    max_x : int
    max_y : int
    def __init__(self, max_x, max_y):
        if max_x <= 0 and max_y <= 0:
            raise ValueError("Cannot construct zero or negative sized plateau")
        self.max_x = max_x
        self.max_y = max_y
 
    def contains(self, position):
        return 0 <= position.x <= self.max_x and \
               0 <= position.y <= self.max_y
