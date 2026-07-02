# jcompressor.py
# JCompressor przebudowany pod F4-RED (252 stany)
# Kompresja = redukcja ramienia + utrzymanie dopuszczalności konfiguracji

from dataclasses import dataclass
from typing import List

from filter_252 import F4State, F4Filter252


@dataclass
class JPoint:
    """
    Pojedynczy punkt w przestrzeni TIMDR:
    wektor 9 pierwiastków strukturalnych (ΔS, τ, Λ × 3 ramiona) w stanie ±1.
    """
    bits: List[int]

    def to_f4_state(self) -> F4State:
        return F4State(bits=self.bits)


class JCompressor:
    """
    JCompressor:
    - wykonuje redukcję jednego ramienia (kompresja strukturalna)
    - utrzymuje stan w dopuszczalnej przestrzeni 252 konfiguracji F4-RED
    """

    def __init__(self):
        self.filter = F4Filter252()

    def _reduce_arm(self, point: JPoint) -> JPoint:
        """
        Redukcja jednego ramienia:
        Tu możesz wstawić swoją właściwą logikę kompresji.
        Na razie: placeholder — nie zmienia wektora.
        """
        # TODO: podmień na swoją realną transformację redukcji ramienia
        return point

    def compress(self, point: JPoint) -> JPoint | None:
        """
        Główna operacja:
        - redukcja ramienia
        - walidacja F4-RED (252 stany)
        - zwrot skompresowanego punktu albo None, jeśli stan jest niedopuszczalny
        """
        reduced = self._reduce_arm(point)
        state = reduced.to_f4_state()

        if self.filter.apply(state):
            return reduced
        return None

    def stats(self) -> dict:
        return self.filter.stats()
