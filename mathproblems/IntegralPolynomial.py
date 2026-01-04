from .Utils import Utils
from .MathProblem import MathProblem
from .IntegralProblem import IntegralProblem

class IntegralPolynomial(IntegralProblem):
    def __init__(self, degree: int):
        super().__init__()
        self.degree = degree
    
    def _get_expression(self):
        return Utils.polynomial(self.degree)
