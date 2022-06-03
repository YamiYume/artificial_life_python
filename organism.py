from random import random
from itertools import chain
from more_itertools import sliced
from bitstring import BitArray

from genome import Genome


class Organism:

    __slots__ = ('adn', 'brain', 'coordinates', 'ecosystem',
                 'ecosystem_size')

    input_neurons = None
    middle_neurons = None
    output_neurons = None
    genome_size = 0

    def __init__(self, ecosystem, parent_genome=None):
        self.adn = Genome(self.genome_size, parent_genome)
        self.ecosystem = ecosystem
        self.ecosystem_size = ecosystem.ecosystem_size
        self.coordinates = [int(random() * self.ecosystem_size[0]),
                            int(random() * self.ecosystem_size[1])]
        self.brain_creation()
        self.get_subscriptions()

    def brain_creation(self):
        brain = []
        for neuron_list in (self.input_neurons,
                            self.middle_neurons,
                            self.output_neurons):
            brain.append([neuron(self) for neuron in neuron_list])

        genome_decoded = self.decode()

        for gene_read in genome_decoded:

            parent_type = brain[gene_read[0]]
            parent_position = gene_read[1] % len(parent_type)
            parent = parent_type[parent_position]
            child_type = brain[gene_read[2] + 1]
            child_position = gene_read[3] % len(child_type)
            child = child_type[child_position]
            weight = gene_read[4]

            parent.append_child(child, weight)
            child.increase_memory()

        brain = filter(lambda x: x.wiring_check(),
                       [neuron for neuron in chain(*brain)])

        self.brain = tuple(brain)

    def decode(self):
        genome_decoded = []
        for gene in sliced(self.adn.genome, 8):
            gene = format(int(gene, 16), '0>32b')
            gene = (gene[:1],
                    gene[1:8],
                    gene[8:9],
                    gene[9:16],
                    gene[16:])

            gene_read = []

            for step, value in enumerate(gene):
                if step == 4:
                    gene_read.append(BitArray(bin=value).int)
                    continue
                gene_read.append(int(value, 2))

            genome_decoded.append(tuple(gene_read))

        return tuple(genome_decoded)

    def get_subscriptions(self):
        for neuron in self.brain:
            try:
                neuron.get_subscription(self.ecosystem)
            except AttributeError:
                pass

    @classmethod
    def set_input_neurons(cls, input_neurons):
        cls.input_neurons = input_neurons

    @classmethod
    def set_output_neurons(cls, output_neurons):
        cls.output_neurons = output_neurons

    @classmethod
    def set_middle_neurons(cls, middle_neurons):
        cls.middle_neurons = middle_neurons

    @classmethod
    def set_genome_size(cls, genome_size):
        cls.genome_size = genome_size
