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
        """Test 1

        Uses keys and messages of equal length.
        """

        message = [0, 1, 0, 0, 1, 0]
        long_key = [1, 0, 0, 1, 1, 1]

        self.assertEqual(len(message), len(long_key))
        self.assertEqual([1, 1, 0, 1, 0, 1], cipher(message, long_key))

    def test_short_key(self):
        """Test 2
        
        Uses keys that are shorter than the message. The 
        expectation is that the XOR module will use modulo 
        division to repeat the key to match the length of 
        the message
        """

        message = [0, 1, 0, 0, 1, 0]
        short_key = [0, 1]

        self.assertEqual([0, 0, 0, 1, 1, 1], cipher(message, short_key))

    def test_different(self):
        """Test 3 
        
        Asserts the basic XOR logic
        
        p q |
        ----|--
        0 1 | 1
        1 0 | 1
        """

        message = [0, 1, 0, 1]
        key = [1, 0, 1, 0]

        self.assertEqual([1, 1, 1, 1], cipher(message, key))

    def test_same_input_1(self):
        """Test 4 
        
        
        Asserts the basic XOR logic

        p q | 
        ----|--
        1 1 | 0
        """

        message = [1, 1, 1, 1, 1, 1]
        key = [1, 1]

        self.assertEqual([0, 0, 0, 0, 0, 0], cipher(message, key))

    def test_same_input_0(self):
        """Test 5
        
        Asserts the basic XOR logic

        p q | 
        ----|--
        0 0 | 0
        """

        message = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        key = [0, 0, 0, 0, 0]

        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         cipher(message, key))
