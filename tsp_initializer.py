from random import randint

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import RoutesGenotype


class TspInitializer(Operator):
    def __init__(self, routesList, dims=1, size=100):
        super(TspInitializer, self).__init__(RoutesGenotype)
        self.size = size
        self.dims = dims
        self.routesList = routesList
        self.routesListLen = len(self.routesList)

    def process(self, population):
        # print self.routesList
        for i in range(self.size):
            # population.append(Votes([self.__randomize() for _ in range(self.dims)]))
            # print choice(self.votesList)
            toAppend  = RoutesGenotype(self.routesList[randint(0,self.routesListLen - 1)])
            # print(toAppend)
            population.append(toAppend)

        # for p in population:
        #     print p.route

            # def __randomize(self):
            #     return randint(self.lowerbound, self.upperbound)