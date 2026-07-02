# rotation.py — przebudowany pod filtr F4-RED

from pc_filter_layer import PCFilterLayer

pc_filter = PCFilterLayer()

class Rotation:
    def __init__(self):
        pass

    def _internal_rotation(self, state):
        return state

    def rotate(self, state_vector):
        new_state = self._internal_rotation(state_vector)

        if pc_filter.validate(new_state):
            return new_state
        return None
