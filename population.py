import random
from individual import Individual


class Population(object):
    def __init__(self, size):
        self.size = size
        self.individuals: list[Individual] = []

    def create_population(self, individual_size):
        for _ in range(self.size):
            individual = Individual(individual_size)
            individual.create_genes()
            self.individuals.append(individual)

    def evaluate_fitness(self, target):
        for individual in self.individuals:
            individual.calculate_fitness(target)

    def crossover(self):
        cross_generation = []

        fittest = sorted(self.individuals,
                         key=lambda x: x.fitness, reverse=True)

        # 10% of the population will go to the next generation
        elitism_rate = int(self.size * 0.1)
        cross_generation.extend(fittest[:elitism_rate])

        # 50% of the population will mate
        mate = int(self.size * 0.5)
        for _ in range(mate):
            parent1 = random.choice(fittest[:self.size//2])
            parent2 = random.choice(fittest[:self.size//2])

            child = parent1.mate(parent2)
            cross_generation.append(child)

        self.individuals = cross_generation

    def get_result(self):
        return "".join(self.individuals[0].genes)

    def get_fittest(self):
        return self.individuals[0].fitness
