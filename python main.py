from dataclasses import dataclass

@dataclass
class TriangleState:
    name: str
    value: float

class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.states = [
            TriangleState("A", a),
            TriangleState("B", b),
            TriangleState("C", c),
        ]

    def as_vector(self):
        return tuple(s.value for s in self.states)
