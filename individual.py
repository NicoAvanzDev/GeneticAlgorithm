import random
import string


class Individual(object):
    def __init__(self, size):
        self.size = size
        self.genes = []
        self.fitness = 0

    def create_genes(self):
        for _ in range(self.size):
            self.genes.append(self.__get_random_gene())

    def calculate_fitness(self, target):
        fitness = 0
        for a, b in zip(self.genes, target):
            if a == b:
                fitness += 1
        self.fitness = fitness

    def crossover(self, other):
        child: Individual

        half = self.size//2

        child = self.genes[half:] + other.genes[:half]

        return child

    def mate(self, other):
        child = Individual(self.size)

        for a, b in zip(self.genes, other.genes):
            prob = random.random()

            if prob < 0.45:
                child.genes.append(a)
            elif prob < 0.9:
                child.genes.append(b)
            else:
                child.genes.append(self.__get_random_gene())

        return child

    def __get_random_gene(self):
        return random.choice(
            string.ascii_letters + string.punctuation + ' ')
