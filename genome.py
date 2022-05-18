from random import getrandbits, random


class Genome:
    '''
     Class in charge of generate and manipulate a hex string
     genome that codifies the brain structure of a Organism
    '''

    __slots__ = ('genome', 'genome_size')

    def __init__(self, genome_size: int, inheritance: str = None):
        '''
        __init__ Create a instance of the genome given how much
        genes it have or copy it if one is provide.

        Args:
            genome_size (int): Number of gene in the genome.
            inheritance (str, optional): Genome to inherit.
                                         Defaults to None.
        '''
        if inheritance is None:
            genome = ''
            for _ in range(genome_size):
                gene = format(getrandbits(32), '0>8x')
                genome += gene
            self.genome = gene
        else:
            self.genome = inheritance
            self.genome_size = genome_size

    def mutate(self, probability: float):
        '''
        mutate Mutate a genome with a given probability

        Args:
            probability (float): How likely is to mutate
        '''
        if random() < probability:
            new_allele = format(int(random() * 16), 'x')
            position = int(random() * 8 * self.genome_size)
            genome = [*self.genome]
            genome[position] = new_allele
            self.genome = ''.join(genome)
