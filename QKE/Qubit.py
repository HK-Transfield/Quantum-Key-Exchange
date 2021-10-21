#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "Harmon Transfield"
# ---------------------------------------------------------------------------
"""A model of a a qubit (quantum bit)
    
When instantiated, the qubit is encoded with a photon's
polarization. There are two types of polarizations,
circular and linear, which are orthogonal to each other.

Qubits are encoded via a photon's polarization:
    Circular:
        - 1 = Counterclockwise polarization
        - 0 = Clockwise polarization
    Linear:
        - 1 = Upwards polarization
        - 0 = Downwards polarization
"""
# ---------------------------------------------------------------------------

import random


class Qubit:
    """A class to represent a Qubit"""
    def __init__(self, val: int, pol: int):
        """Constructor. Instantiates a new Qubit object

        Parameters
        ----------
        val : int 
            A randomized bit
        pol : int
            A representation of a photon polarization
        
        """

        self.value = val
        self.polarization = pol

    def set(self, val: int, pol: int):
        """Changes the value and polarization 

        This method would not be used in a standard
        QKE exchange between transmitter and receiver.
        This is only used for testing purposes and
        when calling Qubit.Measure()

        Parameters
        ----------
        val : int 
            A randomized bit
        pol : int
            A representation of a photon polarization
        """

        self.value = val
        self.polarization = pol

        return None

    def measure(self, pol: int) -> int:
        """Measures qubits through a polarization filter.

        If a photon of a qubit is polarized in a circular manner,
        it has an equal 50/50 chance to be measured as upwards or
        downwards when measured linearly (and vice-versa when 
        measured circularly).

        Parameters
        ----------
        pol : int 
            The polarization used to filter the qubit

        Returns
        ----------
        int 
            Value if polarizations match or random 50/50 value if they do not
        """

        if self.polarization == pol:
            return self.value

        else:

            # New value has 50/50 change
            rand_value = 1 if random.random() < 0.5 else 0
            self.set(rand_value, pol)

            return self.value
