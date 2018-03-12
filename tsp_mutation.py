import random

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import RoutesGenotype


class AbstractMutation(Operator):
    def __init__(self, type, probability):
        super(AbstractMutation, self).__init__()
        self.probability = probability

    def process(self, population):
        for genotype in population:
            if random.random() < self.probability:
                self.mutate(genotype)

class TspMutation(AbstractMutation):
    def __init__(self, probability, evol_probability):
        super(TspMutation, self).__init__(RoutesGenotype, evol_probability)
        self.probability = probability

    def mutate(self, genotype):
        # logger.debug("Mutating genotype: {0}".format(genotype))
        rand1 = random.randint(0, len(genotype.route) - 1)
        rand2 = random.randint(0, len(genotype.route) - 1)
        genotype.route[rand1], genotype.route[rand2] = genotype.route[rand2], genotype.route[rand1]

        # for vote in genotype.votes:
        #     rand = random.random()
        #     index_of_cand = vote.index(genotype.candidate)
        #     if rand < self.probability:
        #         bias = random.randint(-10,10)
        #         biased = (index_of_cand-bias)%len(vote)
        #         vote.insert(biased, vote.pop(index_of_cand))