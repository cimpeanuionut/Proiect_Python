import itertools
import numpy as np
from sklearn import cluster

class Clustering:
    def __init__(self):
        pass

    def acluster(self, row_names, col_names, data):
        numpy_data = np.array(data)
        clustered = cluster.AgglomerativeClustering(compute_full_tree=True, n_clusters=2, linkage='complete')
        model = clustered.fit(numpy_data)

        it = itertools.count(numpy_data.shape[0])
        clusters = [{'id': next(it), 'left': x[0], 'right': x[1]} for x in model.children_]
        self.print_cluster(clusters, clusters[-1]['id'], numpy_data.shape[0], labels=row_names)

    def print_cluster(self, clusters, current_id, initial_value, labels=None, n=0):
        for i in range(n):
            print(' ', end='')
        if current_id < initial_value:
            if labels == None:
                print(current_id)
            else:
                print(labels[current_id])
        else:
            print('-')
            current_cluster = [c for c in clusters if current_id == c['id']][0]
            self.print_cluster(clusters, current_cluster['left'], initial_value, n=n + 1, labels=labels)
            self.print_cluster(clusters, current_cluster['right'], initial_value, n=n + 1, labels=labels)