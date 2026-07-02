def test_motion_rotation():
    from core.motion import MotionState
    from core.rotation import RotationOperator
    state = MotionState()
    rot = RotationOperator(state)
    assert rot.angle >= 0
