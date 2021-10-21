#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""Unit tests for the Channel module.

This test emulates the QKE algorithm, followed by the secure exchange of a 
symmetrically encrypted message using the key produced by QKE.

It is then followed with a confidentiality man-in-the-middle attack to test
if it is possible to decpiher the exchanged secret message.
"""
# ---------------------------------------------------------------------------

from unittest import TestCase
from QKE.Emulation import QKEEmulator

emulate_standard = QKEEmulator(qubit_length=16)
emulate_intercept = QKEEmulator(qubit_length=16, run_type="intercept")
emulate_mitm = QKEEmulator(qubit_length=16, run_type="attack")


class TestQKE(TestCase):
    def test_QKE(self):
        QKE_results = emulate_standard.run_QKE()
        self.assertTrue(QKE_results)

    def test_symmetric_encryption(self):
        encryption_results = emulate_standard.run_symmetric_encryption()
        self.assertTrue(encryption_results)

    def test_intercept_resend(self):
        intercept_results = emulate_intercept.run_QKE()
        self.assertFalse(intercept_results)

    def test_mitm_QKE(self):
        mitm_QKE_results = emulate_mitm.run_QKE()
        self.assertTrue(mitm_QKE_results)

    def test_mitm_encryption(self):
        mitm_encryption_results = emulate_mitm.run_symmetric_encryption()
        self.assertTrue(mitm_encryption_results)