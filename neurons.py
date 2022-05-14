import abc


class Neuron(abc.ABC):

    @abc.abstractclassmethod
    def __init__(self) -> None:
        pass


class InputNeuron(Neuron):

    def __init__(self, child_links: dict) -> None:
        self.childs_links = child_links
        self.calculation = None

    @abc.abstractclassmethod
    def input_calculation(self, **kwargs) -> None:
        pass

    def output_sending(self) -> None:
        for neuron, weight in self.childs_links.items():
            neuron.neuron_memory.add_memory(self.calculation * weight)
        self.calculation = None


class InputLifetime(InputNeuron):

    def input_calculation(self, **kwargs) -> None:
        self.calculation = kwargs['bit_lived']
