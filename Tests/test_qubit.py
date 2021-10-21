#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""Unit tests for the Qubit module."""
# ---------------------------------------------------------------------------

from unittest import TestCase
from QKE.Qubit import Qubit

# Create a new qubit for testing purposes
qubit = Qubit(0, 0)
polarization = 0


class TestQubit(TestCase):
    def test_measure(self):
        result = qubit.measure(polarization)
        self.assertEqual(0, result)

    def test_set(self):
        qubit.set(1, 0)

        result = qubit.measure(polarization)
        self.assertEqual(1, result)
