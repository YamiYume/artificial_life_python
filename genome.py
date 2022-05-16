from random import random
from typing import Tuple


class Genome:

    __slots__ = ('genome', 'neuronal_sizes', 'size')

    neuronal_sizes = None
    size = None

    def __init__(self):
        self.genome = tuple()

    def generate_parent_genes(self) -> Tuple[int, int]:

        parent_type = int(random() * 2)
        parent_id = int(random() * self.neuronal_sizes[parent_type])

        return (parent_type, parent_id)

    def generate_child_genes(self) -> Tuple[int, int]:

        child_type = int(random() * 2)
        child_id = int(random() * self.neuronal_sizes[child_type + 1])

        return (child_type, child_id)

    def generate_weight_gene() -> Tuple[int]:

        weight = int((random() * 10 + 1) * -1 ** int(random() * 2))

        return (weight,)

    def generate_genome(self, inherited_genome) -> None:

        if inherited_genome is None:
            for _ in range(self.size):
                parent_genes = self.generate_parent_genes
                child_genes = self.generate_child_genes
                weight_gene = self.generate_weight_gene
                self.genome = self.genome + (parent_genes
                                             + child_genes
                                             + weight_gene,)
        else:
            self.Genome = inherited_genome

    def mutate(self, probability: float) -> None:

        if random() < probability:
            portion = int(random() * 3)
            if portion == 0:
                self.genome = self.generate_parent_genes() + self.genome[2:]
            elif portion == 1:
                self.genome = (self.genome[:2] + self.generate_child_genes()
                               + self.genome[4:])
            else:
                self.genome = self.genome[:4] + self.generate_weight_gene()

    @classmethod
    def set_neuronal_sizes(cls, neuronal_sizes):
        cls.neuronal_sizes = neuronal_sizes

    @classmethod
    def set_size(cls, size: int):
        cls.size = size
