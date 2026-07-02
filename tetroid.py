# tetroid.py — przebudowany pod filtr F4-RED

from pc_filter_layer import PCFilterLayer

pc_filter = PCFilterLayer()

class Tetroid:
    def __init__(self):
        pass

    def evolve(self, state_vector):
        new_state = self._internal_evolve(state_vector)

        if pc_filter.validate(new_state):
            return new_state
        return None

    def _internal_evolve(self, state):
        return state
