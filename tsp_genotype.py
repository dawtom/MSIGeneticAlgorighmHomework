class RoutesGenotype(object):
    def __init__(self, route):
        # example: route = [(1,city.x, city.y),(2,city2x,city2y)]
        self.route = route
        self.fitness = None

    def __str__(self):
        return "{0}\nfitness: {1}".format("\n".join(map(str, self.route)), self.fitness)

