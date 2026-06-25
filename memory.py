from dataclasses import dataclass

@dataclass
class TransitionMemoryEntry:
    twist_deltas: list
    rotation_delta: float
    motion_energy: float
    motion_tension: float
    j_energy: float
    j_tension: float
    j_stability: float

class TransitionMemory:
    def __init__(self, max_size=5000):
        self.max_size = max_size
        self.memory = []

    def add(self, twists, rotation, motion, j_point):
        entry = TransitionMemoryEntry(
            [t.delta for t in twists],
            rotation.total_delta,
            motion.energy,
            motion.tension,
            j_point.compressed_energy,
            j_point.compressed_tension,
            j_point.stability
        )
        self.memory.append(entry)
        if len(self.memory) > self.max_size:
            self.memory.pop(0)

    def last(self):
        return self.memory[-1] if self.memory else None
