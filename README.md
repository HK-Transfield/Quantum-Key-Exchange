# Quantum-Key Exchange

Symmetric-key cryptography requires a shared key to be known between the two parties. A simple
way to encrypt a message is XOR encryption. This method repeatedly applies the XOR operation
on the message using the key. The receiver performs the same operation to decipher the message.

But how does one transmit a key over an insecure channel? Sending it as plain text means it can
be intercepted by a malicious eavesdropper. And we can’t encrypt it because it leads to a chicken-
and-egg problem, since this operation would also require a key.

A classical solution to this problem is Diffie-Helman key-exchange algorithm. With the advent of
quantum computing, however, novel technologies have been developed. Quantum computing
manipulates quantum bits (qubits), instead of classical bits. Qubits are subject to quantum
mechanical laws of physics. In this assignment, you’ll implement and test the Quantum Key
Exchange (QKE) algorithm.

QKE assumes the existence of a quantum communication channel over which qubits can be
transferred. A qubit can be encoded via a photon’s polarization. For example, we can define
counterclockwise polarization ↺ as 1, and clockwise polarization ⟳ as 0. However, this is not the
only option, a photon could also be polarized in a linear fashion; thus, we can define an upwards
polarization ↑ as 1, and a downwards polarization ↓ as 0. Crucially, because of quantum mechanics,
the internal state of a qubit can only be measured by interacting with it through a polarization filter
of a specific type.

|                          | Qubit Value 1 | Qubit Value 2 |
| ------------------------ | ------------- | ------------- |
| **Linear Polarization**  | ↑             | ↓             |
| **Cirular Polarization** | ↻             | ↺             |

The key quantum mechanical observation is that these two types of polarization (circular vs. linear)
are orthogonal to each other. This means that if a photon is polarized in a circular manner, it has
an equal 50-50 chance to be measured as ↑ or ↓ when measured linearly (and vice-versa).

## QKE Algorithm

1. The transmitter sends a stream of qubits and for each, it records the value and polarization
   type, which are both picked randomly with equal chances.

2. The receiver receives the stream of qubits and for each, it selects a random polarization
   type to measure it, and records the results

3. The transmitter and receiver exchange the polarization types the used for the stream. The
   secret key is formed by the recorded qubit values where both happened to use the same
   polarization type. Thus, for these qubits both have recorded the same value but none but
   they know what that value actually is

---

## Installing and running the program

To run program

```
git clone https://github.com/HK-Transfield/Quantum-Key-Exchange
cd Quantum-Key-Exchange
python3 Main.py
```

To run tests

```
git clone https://github.com/HK-Transfield/Quantum-Key-Exchange
cd Quantum-Key-Exchange
pip install -r Requirements.txt
python3 -m pytest
```
