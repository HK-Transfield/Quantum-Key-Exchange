from unittest import TestCase
from numpy.random import randint
import numpy as np
from QKE import Communication

qubit_length = 16
quantum_channel = Communication.QuantumChannel(qubit_length)


class TestingExchange(TestCase):
    def test_encryption(self):
        alice_vals = randint(2, size=qubit_length)
        alice_pols = randint(2, size=qubit_length)

        print("Alice's random values: {}".format(alice_vals))
        print("Alice's random polarizations: {}".format(alice_pols))

        quantum_channel.encode_qubits(alice_vals, alice_pols)

        bob_pols = randint(2, size=qubit_length)
        bob_measurements = quantum_channel.measure_qubits(bob_pols)

        print("Bob's random polarizations: {}".format(bob_pols))
        print("measured : {}".format(bob_measurements))

        alice_key = quantum_channel.generate_key(alice_pols, bob_pols,
                                                 alice_vals)
        bob_key = quantum_channel.generate_key(alice_pols, bob_pols,
                                               bob_measurements)

        # Test 1: Check that Alice and Bob have generated the same keys
        self.assertEqual(alice_key, bob_key)