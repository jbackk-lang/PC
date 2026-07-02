# memory.py — przebudowany pod filtr F4-RED

from pc_filter_layer import PCFilterLayer

pc_filter = PCFilterLayer()

class TransitionMemory:
    def __init__(self):
        self.entries = []

    def push(self, state_vector):
        if pc_filter.validate(state_vector):
            self.entries.append(state_vector)
            return True
        return False

    def get(self):
        return self.entries
