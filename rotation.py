from dataclasses import dataclass

@dataclass
class Rotation:
    cycle_twists: list
    total_delta: float
    net_direction: int

class RotationOperator:
    @staticmethod
    def build_cycle(twists):
        total_delta = sum(t.delta for t in twists)
        net_direction = 1 if total_delta > 0 else -1 if total_delta < 0 else 0
        return Rotation(twists, total_delta, net_direction)
