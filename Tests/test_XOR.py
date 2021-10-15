#!/usr/bin/env python3

from Exchange import XOR
from unittest import TestCase


class TestXOR(TestCase):
    def test_long_key(self):
        message = [0, 1, 0, 0, 1, 0]
        long_key = [1, 0, 0, 1, 1, 1]

        self.assertEqual([1, 1, 0, 1, 0, 1], XOR.cipher(message, long_key))

    def test_short_key(self):
        message = [0, 1, 0, 0, 1, 0]
        short_key = [0, 1]

        self.assertEqual([0, 0, 0, 1, 1, 1], XOR.cipher(message, short_key))

    def test_different(self):
        message = [0, 0, 0, 0]
        key = [1, 1, 1, 1]

        self.assertEqual([1, 1, 1, 1], XOR.cipher(message, key))

    def test_same_input(self):
        message = [1, 1, 1, 1, 1, 1]
        key = [1, 1]

        self.assertEqual([0, 0, 0, 0, 0, 0], XOR.cipher(message, key))