#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""
QKE assumes the existence of a quantum communication channel over which qubits
can be transferred between a transmitter and receiver, as well as any malcious
third parties that may be listening. 

This module assumes that the channel will be insecure, and thus there is no
methods for authenticating entites using the channel. 
"""
# ---------------------------------------------------------------------------

from numpy.random import randint
from .Qubit import Qubit
from .XOR import cipher


class QuantumChannel:
    """
    A class to represent a quantum communication channel where qubits
    can be transferred and received. 
    """
    def __init__(self, ql: int):
        self.stream = []
        self.qubit_length = ql

    ##################################################################
    # GENERAL UTILITIES
    ##################################################################

    def generate_random(self) -> list:
        """Returns a random list of 1s and 0s"""
        return randint(2, size=self.qubit_length).tolist()

    def generate_message(self, message_size: int) -> int:
        """Returns a message as a random list of 1s and 0s"""
        return randint(2, size=message_size).tolist()

    def list_to_string(self, message_list: list) -> str:
        """Concatenates all values of a list into a single string.
        
        Parameters
        ----------
        message_list : list 
            The list to turn into a string
        
        Returns:
        ----------
        str 
            A new string composed of all elements from the list

        """

        # initialize an empty string
        message = ""

        # traverse in the string
        for i in message_list:
            message += str(i)

        # return string
        return message

    ##################################################################
    # QKE UTILITIES
    ##################################################################

    def encode_qubits(self, vals: list, pols: list) -> None:
        """Prepares a stream of qubits to send to a receiver

        For every value the transmitter has, this function encodes
        it passed on the polarizations they have.

        Parameters
        ----------
        vals : list 
            The transmitter's random values
        pols : list 
            The transmitter's random polarizations
        """

        for i in range(self.qubit_length):
            qubit = Qubit(vals[i], pols[i])
            self.stream.append(qubit)

        return None

    def measure_qubits(self, pols: list) -> list:
        """Receiver recieves a stream of qubits.

        The reciever will measure each qubit in the stream
        either linearly, or circularly by apply a random
        set of polarizations to filter the qubits.

        Parameters
        ----------
        pols : list
            The receiver's random polarizations

        Returns
        ----------
        list
            The results of the measurements
        """
        measurements = []

        for i in range(self.qubit_length):
            measurement = self.stream[i].measure(pols[i])
            measurements.append(measurement)

        return measurements

    def generate_key(self, a_pols: list, b_pols: list, vals: list) -> list:
        """Finds a shared key between a transmitter and receiver

        A transmitter and receiver exchange the polarization types they
        used for the quantum channel. The secret key is form by recording
        qubit values where both happened to use the same polarization types.

        Parameters
        ----------
        a_pols : list 
            The transmitter's randomized polarizations
        b_pols : list 
            The reciever's randomized polarizations
        vals : list 
            Either the transmitter's randomized values or 
            the reciever's measured results

        Returns
        ----------
        list 
            A list of all matching positions used as secret key 
        """
        key = []

        for i in range(self.qubit_length):
            if a_pols[i] == b_pols[i]:
                key.append(vals[i])

        return key

    def cipher_message(self, message: list, key: list) -> list:
        """Encrypts (or decrypts) a plain message using a XOR cipher.

        Parameters
        ----------
        message : list
            The plain message to be encrypted
        key : list
            The mask used to encrypt the message

        Returns
        ----------
        list
            The fully encrypted (or decrypted) message

        Raises
        ----------
        TypeError
            This occurs if the cipher fails. The function will return None.
        """
        try:
            return cipher(message, key)
        except TypeError:
            # This error occurs more often when self.qubit_length is really small
            print("Could not decipher anything, no valid key")
