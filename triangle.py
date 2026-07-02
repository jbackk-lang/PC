# triangle.py
# Triangle przebudowany pod F4-RED (252 stany)
# Lokalna projekcja skrętu na 2D, z pełną walidacją dopuszczalności

from dataclasses import dataclass
from typing import List

from filter_252 import F4State, F4Filter252


@dataclass
class TriangleState:
    """
    Lokalna projekcja skrętu:
    reprezentacja 9 pierwiastków strukturalnych (ΔS, τ, Λ × 3 ramiona)
    w formie wektora ±1.
    """
    bits: List[int]

    def to_f4(self) -> F4State:
        return F4State(bits=self.bits)


class Triangle:
    """
    Triangle:
    - lokalna projekcja skrętu Möbiusa
    - operacje 2D na stanie geometrycznym
    - pełna walidacja F4-RED (252 stany)
    """

    def __init__(self):
        self.filter = F4Filter252()

    def _internal_project(self, state: TriangleState) -> TriangleState:
        """
        Tu możesz wstawić swoją właściwą logikę projekcji 2D.
        Na razie: placeholder — nie zmienia wektora.
        """
        # TODO: podmień na swoją realną transformację projekcji
        return state

    def project(self, bits: List[int]) -> TriangleState | None:
        """
        Główna operacja:
        - konwersja do TriangleState
        - projekcja 2D
        - walidacja F4-RED
        - zwrot stanu lub None
        """
        state = TriangleState(bits=bits)
        projected = self._internal_project(state)
        f4 = projected.to_f4()

        if self.filter.apply(f4):
            return projected
        return None

    def stats(self) -> dict:
        return self.filter.stats()
