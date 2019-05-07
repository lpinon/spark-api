from collections import OrderedDict
from tabulate import tabulate


class JobContext(object):
    def __init__(self, sc):
        self.counters = OrderedDict()
        self.sharedData = {}
        self._init_accumulators(sc)
        self._init_shared_data(sc)

    def _init_accumulators(self, sc):
        pass

    def _init_shared_data(self, sc):
        pass

    def initialize_counter(self, sc, name):
        self.counters[name] = sc.accumulator(0)

    def initialize_data_element(self, sc, name, data):
        self.sharedData[name] = sc.broadcast(data)

    def inc_counter(self, name, value=1):
        if name not in self.counters:
            raise ValueError('Counter {0} was not initialized ({1})'.format(name, self.counters.keys()))

        self.counters[name] += value

    def get_data_element(self, name):
        if name not in self.sharedData.keys():
            raise ValueError('Data element {0} was not initialized ({1})'.format(name, self.sharedData.keys()))

        return self.sharedData[name]

    def print_accumulators(self):
        print('aa\n' * 2)
        print(tabulate(self.counters.items(), self.counters.keys(), tablefmt="simple"))
