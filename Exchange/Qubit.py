import random


class Qubit:
    def __init__(self, value, polarization):
        self.value = value
        self.polarization = polarization

    def set(self, value, polarization):
        self.value = value
        self.polarization = polarization
        return None

    def measure(self, polarization):
        if self.polarization == polarization:
            return self.polarization
        else:
            return 1 if random.random() < .5 else 0
