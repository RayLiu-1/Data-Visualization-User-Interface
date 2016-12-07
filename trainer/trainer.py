import pickle

queries_file = "/home/fenfei/Projects/data/se07_lexsub_test_queries_10.pkl"
net_file = "/home/fenfei/Projects/data/se07_lexsub_test_net_info_10.pkl"
class Trainer(object):
    def __init__(self,):
        self.queries = pickle.load(open(queries_file, 'rb'))
        self.net_info = pickle.load(open(net_file, 'rb'))
    def get_data(self, idx):
        assert idx < len(self.queries)
        k = self.queries.keys()[idx]
        part_net = dict()
        q = {}
        for qk in self.queries[k]:
            q[qk] = self.queries[k][qk]
        part_net[q['target']] = self.net_info[q['target']]
        for aw in q['answer']:
            part_net[aw] = self.net_info[aw]
        q['netInfo'] = part_net
        return q
