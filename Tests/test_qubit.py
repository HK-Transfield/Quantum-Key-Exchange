#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "HK Transfield"
# ---------------------------------------------------------------------------
"""
Unit tests for the Qubit module. These tests focus on ensuring that
it returns the correct value when passing in the matching polarizations.
"""
# ---------------------------------------------------------------------------

from unittest import TestCase
from QKE.Qubit import Qubit

# Create a new qubit for testing purposes
qubit = Qubit(0, 0)
polarization = 0


class TestQubit(TestCase):
    def test_measure(self):
        """Test 1

        Asserts that the value inside in the Qubit
        returns 0 when measuring with the same value.
        """

        result = qubit.measure(polarization)
        self.assertEqual(0, result)

    def test_set_1(self):
        """Test 2
        
        Asserts that when setting a new value, 1, into the qubit,
        it will return 1 when the matching polarization, 0, is 
        passed in
        """

        qubit.set(1, 0)

        result = qubit.measure(polarization)
        self.assertEqual(1, result)

    def test_set_0(self):
        """Test 3

        Asserts that when setting a new value, 1, into the qubit,
        it will return 1 when the matching polarization, 1, is 
        passed in 
        """

        polarization = 1

        qubit.set(1, 1)

        result = qubit.measure(polarization)
        self.assertEqual(1, result)
