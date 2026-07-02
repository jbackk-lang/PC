# motion.py — przebudowany pod filtr F4-RED

from pc_filter_layer import PCFilterLayer

pc_filter = PCFilterLayer()

class Motion:
    def __init__(self):
        pass

    def _internal_motion(self, state):
        # Twoja logika ruchu — nie zmieniam
        return state

    def step(self, state_vector):
        new_state = self._internal_motion(state_vector)

        if pc_filter.validate(new_state):
            return new_state
        return None
