import numpy as np

def swap_rows(M, a, b):
    if not isinstance(M, np.ndarray) or M.ndim != 2:
        raise ValueError("M must be a 2D NumPy array")
    if a < 0 or b < 0 or a >= M.shape[0] or b >= M.shape[0]:
        raise ValueError("Invalid row indices")
    M[a], M[b] = M[b].copy(), M[a].copy()
    return M

def swap_cols(M, a, b):
    if not isinstance(M, np.ndarray) or M.ndim != 2:
        raise ValueError("M must be a 2D NumPy array")
    if a < 0 or b < 0 or a >= M.shape[1] or b >= M.shape[1]:
        raise ValueError("Invalid column indices")
    M[:, [a, b]] = M[:, [b, a]]
    return M