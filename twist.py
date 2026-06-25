from dataclasses import dataclass

@dataclass
class Twist:
    from_state: str
    to_state: str
    delta: float
    direction: int

class TwistOperator:
    @staticmethod
    def compute(tetroid):
        twists = []
        for s1, s2 in tetroid.edges():
            delta = s2.value - s1.value
            direction = 1 if delta > 0 else -1 if delta < 0 else 0
            twists.append(Twist(s1.name, s2.name, delta, direction))
        return twists
