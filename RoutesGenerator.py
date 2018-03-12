import random


class RoutesGenerator(object):

    # map is square, its edge is mapDimension
    def __init__(self, numberOfCities, mapDimension, populationSize):
        self.numberOfCities = numberOfCities
        self.mapDimension = mapDimension
        self.populationSize = populationSize

    def __call__(self):
        cities = [(i,random.randint(0,self.mapDimension),random.randint(0,self.mapDimension))
                      for i in range(0,self.numberOfCities)]
        routes = []
        for i in range(0, self.populationSize):
            # random.shuffle(cities)
            # print "Cities:  ", cities
            routes.append(random.sample(cities,len(cities)))
        # for r in routes:
        #     print r
        return routes
        # basis = range(1,self.candidates_nr+1)
        # votes_list = [(random.shuffle(basis), list(basis))[1] for _ in xrange(self.voters_nr)]
        # c_places_list = [vote.index(self.c_nr) for vote in votes_list]
        # random.seed()
        # return votes_list, c_places_list