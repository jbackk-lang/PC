# tests/test_pc_filter_compare.py

import random
from pc_filter_layer import PCFilterLayer

def random_state():
    return [random.choice([-1, 1]) for _ in range(9)]

def test_compare_old_vs_new():
    pc_filter = PCFilterLayer()

    old_pass = 0
    new_pass = 0

    for _ in range(10000):
        s = random_state()

        # stary rdzeń: wszystko przechodzi
        old_pass += 1

        # nowy rdzeń: tylko 252 konfiguracje
        if pc_filter.validate_state(s):
            new_pass += 1

    print("OLD:", old_pass)
    print("NEW:", new_pass)
    print("STATS:", pc_filter.stats())
