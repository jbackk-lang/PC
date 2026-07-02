# twist_operator.py
# TwistOperator przebudowany pod F4-RED (252 stany)
# Operator skrętu Möbiusa w rdzeniu TIMDER

from dataclasses import dataclass
from typing import List

from filter_252 import F4State, F4Filter252


@dataclass
class TwistOpState:
    """
    Stan skrętu:
    9 pierwiastków strukturalnych (ΔS, τ, Λ × 3 ramiona) w stanie ±1.
    """
    bits: List[int]

    def to_f4(self) -> F4State:
        return F4State(bits=self.bits)


class TwistOperator:
    """
    TwistOperator:
    - wykonuje skręt Möbiusa (He → Fe → Og)
    - operuje na 9-bitowych stanach ±1
    - przepuszcza tylko 252 dopuszczalne konfiguracje F4-RED
    """

    def __init__(self):
        self.filter = F4Filter252()

    def _internal_twist(self, state: TwistOpState) -> TwistOpState:
        """
        Tu możesz wstawić swoją właściwą logikę skrętu.
        Na razie: placeholder — nie zmienia wektora.
        """
        # TODO: podmień na swoją realną transformację skrętu Möbiusa
        return state

    def apply(self, bits: List[int]) -> TwistOpState | None:
        """
        Główna operacja:
        - konwersja do TwistOpState
        - wykonanie skrętu Möbiusa
        - walidacja F4-RED (252 stany)
        - zwrot stanu lub None
        """
        state = TwistOpState(bits=bits)
        twisted = self._internal_twist(state)
        f4 = twisted.to_f4()

        if self.filter.apply(f4):
            return twisted
        return None

    def stats(self) -> dict:
        return self.filter.stats()
