#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""Unit tests for the Emulation module.

This test QKE.Emulation module, including the secure exchange of a 
symmetrically encrypted message using the key produced by QKE.

It is then followed with tests for a confidentiality man-in-the-middle attack to test
if it is possible to decpiher the exchanged secret message.
"""
# ---------------------------------------------------------------------------

from unittest import TestCase
from QKE.Emulation import QKEEmulator

emulate_standard = QKEEmulator(qubit_length=16)
emulate_intercept = QKEEmulator(qubit_length=512,
                                message_length=325,
                                run_type="intercept")
emulate_mitm = QKEEmulator(qubit_length=256,
                           message_length=3665,
                           run_type="attack")


class TestQKE(TestCase):
    def test_QKE(self):
        """Test 1
        
        This asserts that the keys generated by Alice and Bob are the same.
        """

        do_keys_match = emulate_standard.run_QKE()
        self.assertTrue(do_keys_match)

    def test_symmetric_encryption(self):
        """Test 2

        This test asserts that Alice and Bob can successfully perform symmetric 
        encryption using the generated secret key. Alice should be able to encrypt 
        a message using that key and send it to Bob, who can then decrypt it with 
        the same key.
        """

        do_messages_match = emulate_standard.run_symmetric_encryption()
        self.assertTrue(do_messages_match)

    def test_intercept_resend(self):
        """Test 3
        
        This test asserts that when Eve intercepts the qubit stream and measures
        them using her own polarizations then it should result in Bob and Alice's
        keys no longer matching.
        """

        intercept_results = emulate_intercept.run_QKE()
        self.assertFalse(intercept_results)

    def test_mitm_QKE(self):
        """Test 4

        This test asserts that if Eve intercepts the qubit stream and measures
        them using Bob's polarizations it will result in the same keys as Bob
        and Alice
        """
        mitm_QKE_results = emulate_mitm.run_QKE()
        self.assertTrue(mitm_QKE_results)

    def test_mitm_encryption(self):
        """Test 5
        
        This test asserts that if Eve has the same key as Alice and Bob, she can
        then decipher the encrypted message sent using the key.
        """
        mitm_encryption_results = emulate_mitm.run_symmetric_encryption()
        self.assertTrue(mitm_encryption_results)