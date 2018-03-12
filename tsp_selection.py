import random
from pyage.core.operator import Operator

class TournamentSelection(Operator):
    def __init__(self, type=None, size=20, tournament_size=20):
        super(TournamentSelection, self).__init__()
        self.size = size
        self.tournament_size = tournament_size

    def process(self, population):
        p = list(population)
        # print "*********************************************************************************"
        # print "*********************************************************************************"
        # print "*********************************************************************************"
        # for x in p:
        #     print x
        # for pp in p:
        #     print pp.route[:10], pp.fitness
        # print self.size
        # print self.tournament_size
        population[:] = []
        for i in range(self.size):
            sample = random.sample(p, self.tournament_size)
            # print i
            # print "*********************************************************************************"
            # print "*********************************************************************************"
            # for s in sample:
            #     print s
            winner = min(sample, key=lambda genotype: genotype.fitness)
            population.append(winner)
            p.remove(winner)


