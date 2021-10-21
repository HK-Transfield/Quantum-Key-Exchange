from .Channel import QuantumChannel

qubit_lengths = [16, 256, 1024]
message_size = 2048  # Use if wanting to have a randomized message


class QKEEmulator:
    def __init__(self, qubit_length: int, run_type: str = None):
        self.qubit_length = qubit_length
        self.qc = QuantumChannel(self.qubit_length)
        self.run_type = run_type
        self.alice_key = None
        self.bob_key = None
        self.eve_key = None

    def run_QKE(self) -> bool:

        # Step 1: Alice generates randoms values and polarizations
        alice_vals = self.qc.set_random()
        alice_pols = self.qc.set_random()

        print(
            "-----------------------------------------------------------------"
        )
        print("Alice's Values\n{}\n".format(alice_vals))
        print("Alice's Polarizations\n{}\n".format(alice_pols))

        # Alice creates qubits and sends them through the stream
        self.qc.encode_qubits(alice_vals, alice_pols)

        # Interception! Eve retrieves qubits and measures them with her own polarizations
        if self.run_type == "intercept":
            eve_pols = self.qc.set_random()
            eve_interception = self.qc.measure_qubits(eve_pols)

            print(
                "-----------------------------------------------------------------"
            )
            print("Eve's Polarizations\n{}\n".format(eve_pols))
            print("Eve's Intercepted Results\n{}\n".format(eve_interception))

        bob_pols = self.qc.set_random()
        bob_measurements = self.qc.measure_qubits(bob_pols)

        print(
            "-----------------------------------------------------------------"
        )
        print("Bob's Polarizations\n{}\n".format(bob_pols))
        print("Bob's Measured Results\n{}\n".format(bob_measurements))

        if self.run_type == "attack":
            eve_interception = self.qc.measure_qubits(bob_pols)
            self.eve_key = self.qc.generate_key(alice_pols, bob_pols,
                                                eve_interception)

            print("Eve's Intercepted Resutls (With Bob's polarization)\n{}\n".
                  format(eve_interception))
            print("Eve's Malicious Key\n{}\n".format(self.eve_key))

        self.alice_key = self.qc.generate_key(alice_pols, bob_pols, alice_vals)
        self.bob_key = self.qc.generate_key(alice_pols, bob_pols,
                                            bob_measurements)
        print(
            "-----------------------------------------------------------------"
        )
        print("Alice's Key\n{}\n".format(self.alice_key))
        print("Bob's Key\n{}\n".format(self.alice_key))

        return self.alice_key == self.bob_key

    def run_symmetric_encryption(self) -> bool:
        try:
            alice_message = self.qc.set_message(message_size)

            alice_cipher = self.qc.cipher_message(alice_message,
                                                  self.alice_key)
            bob_message = self.qc.cipher_message(alice_cipher, self.bob_key)

            print(
                "-----------------------------------------------------------------"
            )
            print("Alice's Message\n{}\n".format(
                self.qc.list_to_string(alice_message)))
            print("Bob's Message\n{}\n".format(
                self.qc.list_to_string(bob_message)))

            if self.run_type == "attack":
                eve_message = self.qc.cipher_message(alice_cipher,
                                                     self.eve_key)

                print("Eve's Cracked Message\n{}\n".format(
                    self.qc.list_to_string(alice_message)))

                return self.qc.list_to_string(
                    alice_message) == self.qc.list_to_string(eve_message)

            return self.qc.list_to_string(
                alice_message) == self.qc.list_to_string(bob_message)

        except TypeError:
            print("Error: No keys have been generated yet!\n")
