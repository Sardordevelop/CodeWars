import numpy as np
def point_vs_vector(point, vector):
    position = -np.sign((vector[1][0] - vector[0][0]) * (point[1] - vector[0][1]) - (vector[1][1] - vector[0][1]) * (point[0] - vector[0][0]))
    return position