from .Problem import Problem
import random
import math

def _get_matrix():
    lam = math.floor(random.random() * 5)
    m = math.floor(random.random() * 5)
    
class LinearPlanarSystemProblem(Problem):
    def __init__(self):
        super().__init__()

    def _get_problem_str(self):
        return "linear planar system"