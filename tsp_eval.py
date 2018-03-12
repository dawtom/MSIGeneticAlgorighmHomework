import math

from pyage.core.operator import Operator
from pyage.tsp.tsp_genotype import RoutesGenotype


class RoutesEvaluator(Operator):
    def __init__(self, type=None):
        super(RoutesEvaluator, self).__init__(RoutesGenotype)

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        # here evaluate routes
        result = 0.0
        routeList = genotype.route
        # print routeList
        for index in range(0, len(routeList) - 1):
            firstCityCoords = routeList[index]
            secondCityCoords = routeList[index + 1]
            result += self.getDistance(firstCityCoords, secondCityCoords)
        return result

    def getDistance(self, oneCity, twoCity):
        # print oneCity
        # print twoCity
        return math.hypot(twoCity[1] - oneCity[1], twoCity[2] - oneCity[2])

