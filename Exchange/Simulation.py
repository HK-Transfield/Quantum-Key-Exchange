# https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html

from Qubit import Qubit
from numpy import random

random.seed(seed=0)
n = 16


def exchange():

    alice_vals = random.randint(2, size=n)
    alice_pols = random.randint(2, size=n)
    alice_message = encode_message(alice_vals, alice_pols)

    bob_pols = random.randint(2, size=n)
    bob_measurements = measure_message(alice_message, bob_pols)


def encode_message(vals, pols):
    message = []

    for i in range(n):
        qubit = qubit(vals[i], pols[i])
        message.append(qubit)

    return message


def measure_message(message, pols):
    measurements = []

    for i in range(n):
        measurement = message[i].measure(pols[i])
        measurements.append(measurement)

    return measurements

def generate_key():


#if __name__ == "__main__":
