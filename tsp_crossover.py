import random

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import RoutesGenotype


class AbstractCrossover(Operator):
    def __init__(self, type, size):
        super(AbstractCrossover, self).__init__(type)
        self.__size = size

    def process(self, population):
        parents = list(population)
        # print "Parents:"
        # for p in parents:
        #     print p.route
        for i in range(len(population), self.__size):
            p1, p2 = random.sample(parents, 2)
            genotype = self.cross(p1, p2)
            population.append(genotype)


class TspCrossover(AbstractCrossover):
    def __init__(self, size):
        super(TspCrossover, self).__init__(RoutesGenotype, size)

    def cross(self, p1, p2):
        firstRoute = p1.route
        secondRoute = p2.route
        # print "First route: ", firstRoute
        # print "Second route: ", secondRoute
        # for x in secondRoute:
        #     print x[0]
        index1 = random.randint(0,len(firstRoute)/2)
        index2 = random.randint(0,len(secondRoute)/2)
        indexBigger = index1 if index1 > index2 else index2
        indexSmaller = index1 if index1 < index2 else index2

        extraction = firstRoute[indexSmaller:indexBigger]
        resultRoute = secondRoute
        # print "Extraction: ", extraction
        for city in extraction:
            resultRoute.remove(city)
        # print "Result route after extraction:   ", resultRoute
        for index in range(indexSmaller, indexBigger):
            resultRoute.insert(index, extraction[index - indexSmaller])
        # print "Result route", resultRoute
        return RoutesGenotype(resultRoute)