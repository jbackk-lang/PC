# rotation.py
# Rotation przebudowany pod F4-RED (252 stany)
# Operator obrotu w triadzie λ-τ-ρ z pełną walidacją dopuszczalności

from dataclasses import dataclass
from typing import List

from filter_252 import F4State, F4Filter252


@dataclass
class RotationState:
    """
    Stan obrotu:
    9 pierwiastków strukturalnych (ΔS, τ, Λ × 3 ramiona) w stanie ±1.
    """
    bits: List[int]

    def to_f4(self) -> F4State:
        return F4State(bits=self.bits)


class Rotation:
    """
    Rotation:
    - obrót stanu w triadzie λ-τ-ρ
    - pełna walidacja F4-RED (252 stany)
    """

    def __init__(self):
        self.filter = F4Filter252()

    def _internal_rotate(self, state: RotationState) -> RotationState:
        """
        Tu możesz wstawić swoją właściwą logikę obrotu.
        Na razie: placeholder — nie zmienia wektora.
        """
        # TODO: podmień na swoją realną transformację obrotu
        return state

    def rotate(self, bits: List[int]) -> RotationState | None:
        """
        Główna operacja:
        - konwersja do RotationState
        - obrót triady λ-τ-ρ
        - walidacja F4-RED
        - zwrot stanu lub None
        """
        state = RotationState(bits=bits)
        rotated = self._internal_rotate(state)
        f4 = rotated.to_f4()

        if self.filter.apply(f4):
            return rotated
        return None

    def stats(self) -> dict:
        return self.filter.stats()
