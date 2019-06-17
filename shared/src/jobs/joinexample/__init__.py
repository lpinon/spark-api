from shared import JobContext


class JoinExampleContext(JobContext):
    def _init_shared_data(self, sc):
        testData = [(1, (1, 2)), (2, (2, 3)), (3, (3, 4))]
        bDataTest = sc.parallelize(testData).collectAsMap()
        self.initialize_data_element(sc, 'test', bDataTest)


def analyze(sc):
    context = JoinExampleContext(sc)
    a = [(1, (-1, -2)), (2, (-2, -3)), (3, (-3, -4))]  # suppose this is the large data set.
    rdd_a = sc.parallelize(a)
    join_a_test = rdd_a.map(lambda kv: (kv[0], context.get_data_element('test').value.get(kv[0], '-'), kv[1]))
    print(join_a_test.take(5))
