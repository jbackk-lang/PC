# pc_filter_layer.py
# Warstwa filtrująca dla rdzenia PC — dopuszcza tylko 252 stany F4-RED

from filter_252 import F4State, F4Filter252


class PCFilterLayer:
    def __init__(self):
        self.filter = F4Filter252()

    def validate(self, state_vector):
        """
        state_vector: lista 9 wartości ±1 wygenerowana przez Motion/Rotation/Twist/Tetroid.
        """
        state = F4State(bits=state_vector)
        return self.filter.apply(state)

    def stats(self):
        return self.filter.stats()
