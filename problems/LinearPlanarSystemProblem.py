from .Problem import Problem
import random, math
import numpy as np

def _e_vect_random() -> int:
    return int(random.random() * 11 - 5)

def _p_random():
    D = 1 # set determinant
    a = int((random.random() * 4 + 1) * math.pow(-1, int(random.random() * 2)))
    c = int(random.random() * 4 + 1)
    d = int(random.random() * 4 + 1)
    numerator = (D + c*d)
    while (a != 1 and a != -1 and numerator % a != 0):
        c = int(random.random() * 4 + 1)
        d = int(random.random() * 4 + 1)
        numerator = (D + c*d)
        print(numerator, numerator % a)
    b = int((numerator) / a)

    # print(f"{a} {b} - {c} {d} = {D}")
    
    return a,b,c,d

def _get_matrix():
    success: bool = True

    # Random eigenvalues
    e_value_1: int = int((random.random() * 4 + 1) * math.pow(-1, int(random.random() * 2)))
    e_value_2: int = int((random.random() * 4 + 1) * math.pow(-1, int(random.random() * 2)))

    a,b,c,d = _p_random()
    diag = np.array([[e_value_1, 0], [0, e_value_2]], np.int32)
    p = np.array([[a, c], [d, b]], np.int32)
    # e_vect_1 = np.ndarray(
    #     [_e_vect_random()],
    #     [math.floor(random.random() * 7 - 3)], np.int32)
    # e_vect_2 = np.ndarray(
    #     [math.floor(random.random() * 7 - 3)],
    #     [math.floor(random.random() * 7 - 3)], np.int32)
    
    result = None
    try:
        result = np.astype(p @ diag @ np.linalg.inv(p), np.int32)
    except np.linalg.LinAlgError:
        success = False
    if (not success):
        result = _get_matrix()

    print(f"P matrix is {p}")
    print(f"Diagonal matrix is {diag}")
    print(f"Result is {result}")
    return result
    
class LinearPlanarSystemProblem(Problem):
    def __init__(self):
        super().__init__()

    def _get_problem_str(self):
        matrix = _get_matrix()
        shape = matrix.shape
        result = "Given this 2x2 matrix:\n"

        # Print out the matrix
        for r in range(shape[0]):
            result += "["
            for c in range(shape[1]):
                result += f"{matrix[r][c]:3d} "
            result += "]\n"

        result += "Find the eigenvalues and eigenvectors.\nIn the context of differential equations, find the general solution of the linear planar system."
        return result