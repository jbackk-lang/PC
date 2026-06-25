import math
from dataclasses import dataclass

@dataclass
class JPoint:
    compressed_energy: float
    compressed_tension: float
    stability: float

class JCompressor:
    @staticmethod
    def compress(motion):
        if motion.energy <= 0:
            return JPoint(0.0, 0.0, 0.0)

        ce = math.log1p(motion.energy)
        ct = motion.tension / (motion.energy + 1e-9)

        base_stability = 1.0 - min(1.0, ct)
        direction_factor = 0.5 if motion.direction == 0 else 1.0
        stability = max(0.0, min(1.0, base_stability * direction_factor))

        return JPoint(ce, ct, stability)
