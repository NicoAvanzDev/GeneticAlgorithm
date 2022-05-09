from population import Population


def main():
    POPULATION = 1000

    TARGET = "The boy who lived, has come to die"

    # Create a population of random individuals
    population = Population(POPULATION)
    population.create_population(len(TARGET))

    generation = 1

    result = ""

    while result != TARGET:
        # Perform crossover and mutation
        population.crossover()

        # Evaluate the fitness of each individual
        population.evaluate_fitness(list(TARGET))

        # Get the fittest individual
        result = population.get_result()

        print(
            f"Generation: {generation}\tResult:{result}\tFitness:{population.get_fittest()}")

        generation += 1


if __name__ == '__main__':
    main()
