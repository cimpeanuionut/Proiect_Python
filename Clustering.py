import itertools
import numpy as np
from sklearn import cluster
import scipy.cluster.hierarchy as sch
from matplotlib import pyplot as plt

class Clustering:
    def __init__(self):
        pass

    # Functia va aplica algoritmul de Agglomerative Clustering
    def acluster(self, row_names, col_names, data):
        numpy_data = np.array(data)
        clustered = cluster.AgglomerativeClustering(compute_full_tree=True, n_clusters=None,
                                                    linkage='complete', distance_threshold=0)
        model = clustered.fit(numpy_data)
        self.plot_dendrogram(model, truncate_mode='level', p=10, labels=row_names)
        plt.show()

        it = itertools.count(numpy_data.shape[0])
        clusters = [{'id': next(it), 'left': x[0], 'right': x[1]} for x in model.children_]
        self.print_cluster(clusters, clusters[-1]['id'], numpy_data.shape[0], labels=row_names)

    # Functia va afisa la consola datele in urma clusterizari
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

    # Functia va realiza dendograma clusterelor
    def plot_dendrogram(self, model, **kwargs):
        counts = np.zeros(model.children_.shape[0])
        n_samples = len(model.labels_)
        for i, merge in enumerate(model.children_):
            current_count = 0
            for child_idx in merge:
                if child_idx < n_samples:
                    current_count += 1
                else:
                    current_count += counts[child_idx - n_samples]
            counts[i] = current_count

        linkage_matrix = np.column_stack([model.children_, model.distances_,
                                          counts]).astype(float)

        # Deseneaza dendograma respectiva
        sch.dendrogram(linkage_matrix, **kwargs)