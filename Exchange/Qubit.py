import random


class Qubit:
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
            return 1 if random.random() < 0.5 else 0