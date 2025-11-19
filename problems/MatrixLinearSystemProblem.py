from .Problem import Problem
import random
import math

class MatrixLinearSystemProblem(Problem):
    def __init__(self, dimension: int = 3):
        self.dimension = dimension
        self.sols = self._generate_solution()
        super().__init__()
    
    def _get_problem_str(self):
        result = "Please solve the following linear system using Gaussian Elimination.\n"
        for i in range(self.dimension):
            result += self._new_equation()
        return result
    
    def _generate_solution(self):
        sols = []
        for i in range(self.dimension):
            ran = math.floor(random.random() * 7 - 3)
            sols.append(ran) 
        return sols
    
    def _new_equation(self) -> str:
        sum = 0
        result = ""
        for component in self.sols:
            coef = math.floor(random.random() * 9 - 4)
            term = coef * component
            sum += term
            result += f"{term:3d} "
        result += f"| {sum:3d}\n"
        return result