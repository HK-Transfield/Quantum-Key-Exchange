#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""
Implements an emulation of the QKE algorithm, followed by the secure exchange
of a symmetrically encrypted message using the key produced by QKE.
"""
# ---------------------------------------------------------------------------

from .Channel import QuantumChannel

qubit_lengths = [16, 256, 1024]
# message_size = 2048


class QKEEmulator:
    """This class represents an emulation of a QKE."""
    def __init__(self,
                 qubit_length: int,
                 message_length: int = 512,
                 run_type: str = None):
        """Constructor. Instantiates a new QKEEmulator.

        Parameters
        ----------
        qubit_length : int
            The maximum number of qubits that will be sent in the stream.
            Used to instantiate a new QuantumChannel.

        message_length : int
            How long the randomly generated message will be
        
        run_type : str (Optional)
            A flag that signals what kind of emulation you want to execute:
            - standard: Executes a QKE without any attacks (default)
            - intercept: Executes a QKE with a intercept-resend MITM attack
            - attack: Executes a QKE with a confidential MITM attack
        """
        self.qc = QuantumChannel(qubit_length)
        self.run_type = run_type
        self.message_length = message_length
        self.alice_key = None
        self.bob_key = None
        self.eve_key = None

    def run_QKE(self) -> bool:
        """Starts a new QKE session.
        
        This algorithm uses 3 characters:
        1. Alice (Transmitter)
        2. Bob (Receiver)
        3. Eve (Eavesdropper)

        Returns
        ----------
        bool
            True if Bob and Alice's keys are matching, or Eve's key matches Alice and Bob's key.
        """

        # Alice generates randoms values and polarizations
        alice_vals = self.qc.generate_random()
        alice_pols = self.qc.generate_random()

        # Alice creates qubits and sends them through the stream
        self.qc.encode_qubits(alice_vals, alice_pols)

        print("------------------------------------------------------")
        print("Alice's Values\n{}\n".format(alice_vals))
        print("Alice's Polarizations\n{}\n".format(alice_pols))
        print("------------------------------------------------------")

        # Interception! Eve retrieves qubits and measures them with her own polarizations
        if self.run_type == "intercept":
            eve_pols = self.qc.generate_random()
            eve_interception = self.qc.measure_qubits(eve_pols)

            print("Eve's Polarizations\n{}\n".format(eve_pols))
            print("Eve's Intercepted Results\n{}\n".format(eve_interception))

        # Bob measures the qubits using his own random polarizations
        bob_pols = self.qc.generate_random()
        bob_measurements = self.qc.measure_qubits(bob_pols)

        print("Bob's Polarizations\n{}\n".format(bob_pols))
        print("Bob's Measured Results\n{}\n".format(bob_measurements))

        # Eve has access to the qubit stream and the exchanged polarizations
        if self.run_type == "attack":
            eve_interception = self.qc.measure_qubits(bob_pols)
            self.eve_key = self.qc.generate_key(alice_pols, bob_pols,
                                                eve_interception)

            print("Eve's Intercepted Results (With Bob's polarization)\n{}\n".
                  format(eve_interception))

        # Alice and Bob generate a secret key and discard the rest of the qubits
        self.alice_key = self.qc.generate_key(alice_pols, bob_pols, alice_vals)
        self.bob_key = self.qc.generate_key(alice_pols, bob_pols,
                                            bob_measurements)

        print("------------------------------------------------------")
        print("Alice's Key\n{}\n".format(self.alice_key))
        print("Bob's Key\n{}\n".format(self.bob_key))

        if self.run_type == "attack":
            print("Eve's Malicious Key\n{}\n".format(self.eve_key))

        if self.eve_key is not None:
            return self.eve_key == self.alice_key and self.eve_key == self.bob_key

        return self.alice_key == self.bob_key

    def run_symmetric_encryption(self) -> bool:
        """Performs a symmetric encryption using a key.

        Returns
        ----------
        bool
            True if Alice and Bob (or Eve) have the same message
        """
        try:
            alice_message = self.qc.generate_message(self.message_length)

            alice_cipher = self.qc.cipher_message(alice_message,
                                                  self.alice_key)
            bob_message = self.qc.cipher_message(alice_cipher, self.bob_key)

            print("------------------------------------------------------")
            print("Alice's Message\n{}\n".format(
                self.qc.list_to_string(alice_message)))
            print("Cipher\n{}\n".format(self.qc.list_to_string(alice_cipher)))
            print("Bob's Message\n{}\n".format(
                self.qc.list_to_string(bob_message)))

            if self.run_type == "attack":
                eve_message = self.qc.cipher_message(alice_cipher,
                                                     self.eve_key)

                print("Eve's Cracked Message\n{}\n".format(
                    self.qc.list_to_string(alice_message)))

                return self.qc.list_to_string(
                    alice_message) == self.qc.list_to_string(
                        eve_message) and self.qc.list_to_string(
                            bob_message) == self.qc.list_to_string(eve_message)

            return self.qc.list_to_string(
                alice_message) == self.qc.list_to_string(bob_message)

        except TypeError:
            print("Error: No keys have been generated yet!\n")
