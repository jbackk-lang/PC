from triangle import Triangle
from tetroid import Tetroid
from twist import TwistOperator
from rotation import RotationOperator
from motion import Motion
from jcompressor import JCompressor
from memory import TransitionMemory

class SkretAI:
    def __init__(self, a, b, c, d):
        self.triangle = Triangle(a, b, c)
        self.tetroid = Tetroid(self.triangle, d)
        self.memory = TransitionMemory()

    def process(self):
        twists = TwistOperator.compute(self.tetroid)
        rotation = RotationOperator.build_cycle(twists)
        motion = Motion.from_rotation(rotation)
        j_point = JCompressor.compress(motion)

        self.memory.add(twists, rotation, motion, j_point)
        return j_point
