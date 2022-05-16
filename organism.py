from genome import Genome
from random import random


class Organims:

    __slots__ = ('adn', 'coordinates', 'ecosystem_size',
                 'input_neurons', 'middle_neurons',
                 'output_neurons')

    ecosystem_size = None

    input_neurons = None
    middle_neurons = None
    output_neurons = None

    def __init__(self, parent_genome=None):
        self.adn = Genome()
        self.adn.generate_genome(parent_genome)
        self.coordinates = [int(random() * self.ecosystem_size[0]),
                            int(random() * self.ecosystem_size[0])]

    @classmethod
    def set_ecosystem_size(cls, ecosystem_size):
        cls.ecosystem_size = ecosystem_size

    @classmethod
    def set_input_neurons(cls, input_neurons):
        cls.input_neurons = input_neurons

    @classmethod
    def set_output_neurons(cls, output_neurons):
        cls.output_neurons = output_neurons

    @classmethod
    def set_middle_neurons(cls, middle_neurons):
        cls.middle_neurons = middle_neurons
