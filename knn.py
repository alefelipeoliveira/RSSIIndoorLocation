import pandas as pd
import copy
from statistics import mean
from error import error

def euclidean(A, B):
    return ( ( (A[0] - B[0])**2 + (A[1] - B[1])**2 + (A[2] - B[2])**2 )**0.5 )

def nearest_index(neighbors, k):
    original_list = copy.copy(neighbors)
    nearest = []
    for i in range(0,k):
        nearest.append(min(neighbors))
        neighbors.remove(min(neighbors))
    nearest = [original_list.index(i) for i in nearest]
    return (nearest)

def knn(dataset, testset, k):
    x_calc, y_calc, error_list = [], [], []
    columns = list(dataset.columns[3:])
    for u in range(0, len(testset['RSSI A'])):
        test_point = []
        for i in columns:
            test_point.append(testset[i][u])
        distances = []

        for i in range(len(dataset['RSSI A'])):
            recorded_point = [dataset['RSSI A'][i], dataset['RSSI B'][i], dataset['RSSI C'][i]]
            distances.append(euclidean(test_point, recorded_point))

        nearest = nearest_index(distances, k)

        x_nearest, y_nearest = list(dataset['x'][nearest]), list(dataset['y'][nearest])
        x, y = mean(x_nearest), mean(y_nearest)
        x_calc.append(x)
        y_calc.append(y)
        error_list.append(error(x, testset['x'][u], y, testset['y'][u]))
    
    testset['x_calc'], testset['y_calc'], testset['error']  = x_calc, y_calc, error_list
    return testset



