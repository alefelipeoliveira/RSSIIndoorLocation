import math

def calculate_distance(RSSI, n, C):
    distance = 10 ** ( (C - RSSI) / (10 * n) )
    return distance