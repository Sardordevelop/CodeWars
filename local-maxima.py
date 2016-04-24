import numpy as np
from scipy.signal import argrelextrema


print argrelextrema(np.array([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]), np.greater)[0]