# tests/test_pipeline_timdr.py
# Test integracyjny całego pipeline TIMDR przez filtr F4-RED (252 stany)

import random

from motion import Motion
from rotation import Rotation
from twist_operator import TwistOperator
from tetroid import Tetroid
from triangle import Triangle
from skret_ai import SkretAI
from memory import TransitionMemory
from pc_filter_layer import PCFilterLayer


def random_state():
    return [random.choice([-1, 1]) for _ in range(9)]


def test_pipeline_timdr():
    motion = Motion()
    rotation = Rotation()
    twist = TwistOperator()
    tetroid = Tetroid()
    triangle = Triangle()
    skret = SkretAI()
    memory = TransitionMemory()
    pc_filter = PCFilterLayer()

    accepted = 0
    rejected = 0

    for _ in range(5000):
        state = random_state()

        # Motion
        state = motion.step(state)
        if state is None:
            rejected += 1
            continue

        # Rotation
        state = rotation.rotate(state.bits)
        if state is None:
            rejected += 1
            continue

        # TwistOperator
        state = twist.apply(state.bits)
        if state is None:
            rejected += 1
            continue

        # Tetroid
        state = tetroid.evolve(state.bits)
        if state is None:
            rejected += 1
            continue

        # Triangle
        state = triangle.project(state.bits)
        if state is None:
            rejected += 1
            continue

        # SkretAI
        state = skret.process(state.bits)
        if state is None:
            rejected += 1
            continue

        # Memory zapisuje tylko dopuszczalne stany
        if memory.push(state.bits):
            accepted += 1
        else:
            rejected += 1

    print("ACCEPTED:", accepted)
    print("REJECTED:", rejected)
    print("FILTER:", pc_filter.stats())
    print("MEMORY:", memory.get())

    assert accepted > 0
    assert rejected > 0
