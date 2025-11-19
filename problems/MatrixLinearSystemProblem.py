from .Problem import Problem
import random
import math

class MatrixLinearSystemProblem(Problem):
    def __init__(self, dimension: int = 3):
        self.dimension = dimension
        super().__init__()
    
    def _get_problem_str(self):
        result = ""
        for i in range(self.dimension):
            result += self._new_equation()
        return result
    
    def _new_equation(self) -> str:
        sum = 0
        result = ""
        for i in range(self.dimension):
            chosen = math.floor(random.random() * 7 - 3)
            coef = math.floor(random.random() * 7 - 3)
            term = coef * chosen
            sum += term
            result += f"{term:03d} "
        result += f"{sum}\n"
        return result