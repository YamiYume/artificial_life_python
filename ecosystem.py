from typing import Tuple

from numpy.random import choice

from organism import Organism

from position_manager import PositionManager


class Ecosystem:

    __slots__ = ('lifespan', 'lifetime', 'population_size', 'ecosystem_size',
                 'mutation_probability', 'population', 'subscribers',
                 'position_manager')

    def __init__(self, lifespan: int, population_size: int,
                 ecosystem_size: Tuple[int, int],
                 mutation_probability: float):

        self.subscribers = {}

        self.lifespan = lifespan
        self.population_size = population_size
        self.ecosystem_size = ecosystem_size
        self.mutation_probability = mutation_probability

        self.lifetime = 0

    def populate(self, survivors: tuple = None):
        population = []

        if survivors is None:

            for _ in range(self.population_size):
                new_organism = Organism(self)
                population.append(new_organism)

        else:
            population_quantitities = divmod(self.population_size,
                                             len(survivors))

            for _ in range(population_quantitities[0]):
                for survivor in survivors:
                    new_organism = Organism(self, survivor.adn.genome)
                    new_organism.adn.mutate(self.mutation_probability)
                    population.append(new_organism)

            for survivor in choice(survivors, population_quantitities[1]):
                new_organism = Organism(self.ecosystem, survivor.adn.genome)
                new_organism.adn.mutate(self.mutation_probability)
                population.append(new_organism)

        self.population = tuple(population)
        self.position_manager = PositionManager(population)

    def subscribe(self, event_type: str, func: callable):

        try:
            self.subscribers[event_type].append(func)
        except KeyError:
            self.subscribers[event_type] = [func]

    def broadcast_event(self, event_type: str, *args):

        for func in self.subscribers[event_type]:
            func(*args)
