import random


class Qubit:
    """A model of a a qubit (quantum bit)
    
    When instantiated, the qubit is encoded with a photon's
    polarization.
    """
    def __init__(self, val, pol):
        self.value = val
        self.polarization = pol

    def set(self, val, pol):
        self.value = val
        self.polarization = pol
        return None

    def measure(self, pol):
        if self.polarization == pol:
            return self.value
        else:
            self.value = 1 if random.random() < 0.5 else 0
            return self.value
