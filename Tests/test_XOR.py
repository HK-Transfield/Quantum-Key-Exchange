#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""Unit tests for the XOR module. This tests all basic functions of XOR operations."""
# ---------------------------------------------------------------------------

from QKE.XOR import cipher
from unittest import TestCase


class TestXOR(TestCase):
    def test_encrypt(self):
        """Tests keys and messages of equal length"""
        message = [0, 1, 0, 0, 1, 0]
        long_key = [1, 0, 0, 1, 1, 1]

        self.assertEqual(len(message), len(long_key))
        self.assertEqual([1, 1, 0, 1, 0, 1], cipher(message, long_key))

    def test_short_key(self):
        """Tests keys that are shorter than the message
        
        The expectation is that the XOR module will use modulo division to
        repeat the key to match the length of the message
        """
        message = [0, 1, 0, 0, 1, 0]
        short_key = [0, 1]

        self.assertEqual([0, 0, 0, 1, 1, 1], cipher(message, short_key))

    def test_different(self):
        """Tests the basic XOR logic T F -> T"""
        message = [0, 0, 0, 0]
        key = [1, 1, 1, 1]

        self.assertEqual([1, 1, 1, 1], cipher(message, key))

    def test_same_input(self):
        """Tests the basic XOR logic T T -> F"""
        message = [1, 1, 1, 1, 1, 1]
        key = [1, 1]

        self.assertEqual([0, 0, 0, 0, 0, 0], cipher(message, key))