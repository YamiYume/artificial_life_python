

from typing import Any

from neurons import InputNeuron


class ResizableTuple():

    def __init__(self, size: int, *args) -> None:
        if args:
            self.resizable_tuple = *args,
        else:
            self.resizable_tuple = tuple()
        self.size = size

    def append(self, value: Any):

        self.__init__(self.size,
                      *self.resizable_tuple, value)

        if len(self.resizable_tuple) == self.size:
            raise IndexError

    def get_values(self):
        return self.resizable_tuple


class Neuron_memory:

    def __init__(self, size, owner: InputNeuron):
        self.memory = ResizableTuple(size)
        self.owner = owner

    def add_memory(self, value):
        try:
            self.memory.append(value)
        except IndexError:
            self.owner.input_calculation(data=self.memory.get_values())
