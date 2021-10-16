from XOR import XOR
import Qubit


class QuantumChannel:
    def __init__(self, ql):
        self.communication_channel = []
        self.qubit_length = ql

    def encode_qubits(self, vals, pols):
        """
        Prepares a stream of qubits to send to a receiver
        """

        for i in range(self.qubit_length):
            qubit = Qubit(vals[i], pols[i])
            self.communication_channel.append(qubit)

    def measure_qubits(self, pols):
        """
        Receiver recieves a stream of qubits, and selects a0
        random polarization to measure it
        """
        measurements = []

        for i in range(self.qubit_length):
            measurement = self.communication_channel[i].measure(pols[i])
            measurements.append(measurement)

        return measurements

    def generate_key(self, a_pols, b_pols, vals):
        """
        Forms a secret key by the 

        """
        key = []

        for i in range(self.qubit_length):
            if a_pols[i] == b_pols[i]:
                key.append(vals[i])

        return key

    def cipher_message(message, key):
        try:
            return XOR.cipher(message, key)
        except TypeError:
            # This error occurs more often when self.qubit_length is really small
            print("Could not decipher anything, no valid key")