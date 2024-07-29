import numpy as np

ar11 = np.array([[6, -9, 1],[4, 24, 8]])

ar21 = np.array([[1, 0],[0, 1]])
ar22 = np.array([[6, -9, 1],[4, 24, 8]])

ar31 = np.array([[4, 3],[2, 3]])
ar32 = np.array([[-2, 3],[3, -4]])

print(np.dot(2, ar11))
print(np.dot(ar21, ar22))
print(np.dot(ar31, ar32))