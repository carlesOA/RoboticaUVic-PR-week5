import os
import numpy as np

print "Solving Q1 and Q2\n"

data = np.array([map(float, x.split(',')[:-3]) for x in open('iris.data') if x.strip()!=''])

def kmeans(data, k, c):
    centroid = []
    centroid = randomize_centroid(data, centroid, k)
    old_centroid = [[] for i in range(k)] 
    iterations = 0

    while not (has_converged(centroid, old_centroid, iterations)):
        iterations += 1
        clusters = [[] for i in range(k)]
        clusters = euclidean_dist(data, centroid, clusters) 
        index = 0
        for cluster in clusters:
            old_centroid[index] = centroid[index]
            centroid[index] = np.mean(cluster, axis=0).tolist()
            index += 1

    print("The means of each cluster are: " + str(centroid))
    return

     
def euclidean_dist(data, centroid, clusters):
    for instance in data:  
        mu_index = min([(i[0], np.linalg.norm(instance-centroid[i[0]]))
	for i in enumerate(centroid)], key=lambda t:t[1])[0] 
	try:
            clusters[mu_index].append(instance)
        except KeyError:
            clusters[mu_index] = [instance]
       
    for cluster in clusters:
        if not cluster:
            cluster.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())

    return clusters


def randomize_centroid(data, centroid, k):
    for cluster in range(0, k):
        centroid.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())
    return centroid

  
def has_converged(centroid, old_centroid, iterations):
    MAX_ITERATIONS = 1000
    if iterations > MAX_ITERATIONS:
        return True
    return old_centroid == centroid


kmeans(data, 2, 5)
