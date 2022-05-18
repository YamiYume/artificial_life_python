from random import random

from numpy import sum as npsum
from numpy import tanh

from organism import Organism
from ecosystem import Ecosystem


class InputNeuron:

    __slots__ = ('child_links', 'calculation', 'owner')

    def __init__(self, owner: Organism) -> None:
        self.owner = owner
        self.child_links = {}
        self.calculation = None

    def input_calculation():
        pass

    def output_sending(self) -> None:
        for child, weight in self.child_links:
            child.input_calculation(self.calculation * weight)

    def append_child(self, child, weight: float):
        self.child_links[child, weight]

    def wiring_check(self):
        removal = []
        wired = False

        for child in self.child_links:
            child_wiring = child.wiring_check()

            if child_wiring is False:
                removal.append(child_wiring)

            wired = wired or child_wiring

        for child in removal:
            del self.child_links[child]

        return wired

    def get_subscription(self, enviroment: Ecosystem):
        enviroment.subscribe(self.__class__.__name__,
                             self.input_calculation)


class OutputNeuron:

    __slots__ = ('calculation', 'owner', 'memory', 'memory_size')

    def __init__(self, owner: Organism) -> None:
        self.owner = owner

        self.memory = []
        self.memory_size = 0
        self.calculation = None

    def input_calculation(self, value) -> None:
        self.memory.append(value)

        if len(self.memory) == self.memory_size:
            self.calculation = tanh(npsum(self.memory))
            self.output_sending()
            self.memory = []

    def output_action():
        pass

    def increase_memory(self):
        self.memory_size += 1

    @staticmethod
    def wiring_check(self):
        if self.memory_size > 0:
            return True
        return False


class MiddleNeuron(InputNeuron):

    __slots__ = ('memory', 'memory_size')

    def __init__(self, owner: Organism) -> None:
        self.memory = []
        self.memory_size = 0

        super().__init__(owner)

    def input_calculation(self, value) -> None:
        self.memory.append(value)

        if len(self.memory) == self.memory_size:
            self.calculation = tanh(npsum(self.memory))
            self.output_sending()
            self.memory = []

    def increase_memory(self):
        self.memory_size += 1

    def get_subscription(self, enviroment: Ecosystem):
        pass


class InputLifetime(InputNeuron):

    def input_calculation(self, bit_lived) -> None:
        self.calculation = bit_lived
        self.output_sending()


class OutputMovementX(OutputNeuron):

    def ouput_actions(self):
        if random() < abs(self.calculation):
            self.owner.coordinate[0] += int(self.calculation
                                            / abs(self.calculation))
