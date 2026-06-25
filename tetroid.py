from dataclasses import dataclass
from triangle import Triangle

@dataclass
class TetraState:
    name: str
    value: float

class Tetroid:
    def __init__(self, triangle: Triangle, d: float):
        a, b, c = triangle.as_vector()
        self.states = [
            TetraState("A", a),
            TetraState("B", b),
            TetraState("C", c),
            TetraState("D", d),
        ]

    def edges(self):
        e = []
        for i in range(len(self.states)):
            for j in range(i + 1, len(self.states)):
                e.append((self.states[i], self.states[j]))
        return e
