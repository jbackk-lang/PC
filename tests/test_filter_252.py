# filter_252.py
# Filtr konfiguracji F4-RED: dopuszcza tylko 252 stany (126 materii + 126 anty)

from dataclasses import dataclass
from typing import List


@dataclass
class F4State:
    """
    Stan F4-RED zapisany jako 9-bitowy wektor (+1 / -1).
    Każdy bit odpowiada jednemu pierwiastkowi strukturalnemu (ΔS, τ, Λ × 3 ramiona).
    """
    bits: List[int]  # długość dokładnie 9, wartości +1 lub -1

    def count_plus(self) -> int:
        return sum(1 for b in self.bits if b == 1)

    def count_minus(self) -> int:
        return sum(1 for b in self.bits if b == -1)

    def is_valid_f4_red(self) -> bool:
        """
        Warunek F4-RED:
        |N_plus - N_minus| <= 1
        oraz dokładnie 9 bitów w stanie ±1.
        """
        if len(self.bits) != 9:
            return False
        if any(b not in (-1, 1) for b in self.bits):
            return False

        n_plus = self.count_plus()
        n_minus = self.count_minus()
        return abs(n_plus - n_minus) <= 1


class F4Filter252:
    """
    Filtr konfiguracji: przepuszcza tylko stany zgodne z F4-RED (252 dopuszczalnych).
    """

    def __init__(self):
        self.accepted = 0
        self.rejected = 0

    def filter_state(self, state: F4State) -> bool:
        """
        Zwraca True, jeśli stan jest dopuszczalny (część 252),
        False, jeśli jest odrzucany.
        """
        if state.is_valid_f4_red():
            self.accepted += 1
            return True
        else:
            self.rejected += 1
            return False

    def stats(self) -> dict:
        return {
            "accepted": self.accepted,
            "rejected": self.rejected,
        }
