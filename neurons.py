from abc import abstractclassmethod, ABC
from numpy import sum, tanh
from random import random


class InputNeuron(ABC):

    __slots__ = ('child_links', 'calculation', 'owner')

    def __init__(self, owner, child_links: dict) -> None:
        self.owner = owner
        self.childs_links = child_links
        self.calculation = None

    @abstractclassmethod
    def input_calculation(self, **kwargs) -> None:
        pass

    def output_sending(self) -> None:
        for child, weight in self.child_links:
            child.input_calculation(self.calculation * weight)


class OutputNeuron(ABC):

    __slots__ = ('calculation', 'owner')

    def __init__(self, owner) -> None:
        self.calculation = None
        self.owner = owner

    def input_calculation(self, **kwargs) -> None:
        self.calculation = tanh(sum(kwargs['data']))
        self.output_action()

    @abstractclassmethod
    def output_action(self) -> None:
        pass


class MemoryHelperNeuron():

    __slots__ = ('child_links', 'memory_size')

    def __init__(self, memory_size, child_links) -> None:
        self.memory_size = memory_size
        self.child_links = child_links
        self.memory = tuple()

    def input_calculation(self, **kwargs):
        self.memory = self.memory + (kwargs['value'],)
        if len(self.memory) == self.memory_size:
            self.output_sending()

    def output_sending(self):
        for child in self.child_links:
            child.input_calculation(data=self.memory)
        self.memory = tuple()


class MiddleNeuron(InputNeuron):

    __slots__ = ('neuron_memory')

    def input_calculation(self, **kwargs) -> None:
        self.calculation = tanh(sum(kwargs['data']))
        self.output_sending()


class InputLifetime(InputNeuron):

    def input_calculation(self, **kwargs) -> None:
        self.calculation = kwargs['bit_lived']
        self.output_sending()


class OutputMovementX(OutputNeuron):

    def ouput_actions(self):
        if random() < abs(self.calculation):
            self.owner.coordinate[0] += int(self.calculation
                                            / abs(self.calculation))
