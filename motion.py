from dataclasses import dataclass

@dataclass
class MotionState:
    energy: float
    tension: float
    direction: int

class Motion:
    @staticmethod
    def from_rotation(rotation):
        abs_sum = sum(abs(t.delta) for t in rotation.cycle_twists)
        pos_sum = sum(t.delta for t in rotation.cycle_twists if t.delta > 0)
        neg_sum = sum(t.delta for t in rotation.cycle_twists if t.delta < 0)
        tension = abs(pos_sum - abs(neg_sum))
        return MotionState(abs_sum, tension, rotation.net_direction)
