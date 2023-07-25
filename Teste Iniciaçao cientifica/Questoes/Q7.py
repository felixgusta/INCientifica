import numpy as np


mat1 = np.random.uniform(low=0.0, high=1.0, size=(3, 3))
print(mat1)


dtm_mat1 = np.linalg.det(mat1)
print(dtm_mat1)