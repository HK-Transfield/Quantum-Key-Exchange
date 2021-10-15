# https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html

from Qubit import Qubit
from numpy import random

# random.seed(seed=0)  # Uncomment if you want to test with the same values every time
n = 16


def main():
    """
    Alice: Transmitter
    Bob: Receiver
    """

    alice_vals = random.randint(2, size=n)
    print("Alice's random values: {}".format(alice_vals))

    alice_pols = random.randint(2, size=n)
    print("Alice's random polarizations: {}".format(alice_pols))

    qubits = encode_qubits(alice_vals, alice_pols)

    bob_pols = random.randint(2, size=n)
    print("Bob's random polarizations: {}".format(bob_pols))

    bob_measurements = measure_qubits(qubits, bob_pols)
    print("Bob's measured values: {}".format(bob_measurements))

    alice_key = generate_key(alice_pols, bob_pols, alice_vals)
    bob_key = generate_key(alice_pols, bob_pols, bob_measurements)

    if alice_key == bob_key:
        print("shared key: {}".format(alice_key))

    message_size = 9
    message = random.randint(n, size=message_size)


def encode_qubits(vals, pols):
    """
    Prepares a stream of qubits to send to a receiver
    """
    qubits = []

    for i in range(n):
        qubit = Qubit(vals[i], pols[i])
        qubits.append(qubit)

    return qubits


def measure_qubits(message, pols):
    """
    Receiver recieves a stream of qubits, and selects a
    random polarization to measure it
    """
    measurements = []

    for i in range(n):
        measurement = message[i].measure(pols[i])
        measurements.append(measurement)

    return measurements


def generate_key(a_pols, b_pols, vals):
    """
    Forms a secret key by the 

    """
    key = []

    for i in range(n):
        if a_pols[i] == b_pols[i]:
            key.append(vals[i])

    return key


if __name__ == "__main__":
    main()