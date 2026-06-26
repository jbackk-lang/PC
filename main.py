from core.motion import MotionState
from core.rotation import RotationOperator
from ai.skret_ai import SkretAI

def run():
    state = MotionState()
    rot = RotationOperator(state)
    ai = SkretAI(rot)
    ai.process()

if __name__ == "__main__":
    run()
