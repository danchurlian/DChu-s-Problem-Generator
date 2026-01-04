from .IntegralProblem import IntegralProblem
from .Utils import Utils
import random

class IntegralSincos(IntegralProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        sin_degree: int = int(random.random() * 6)
        cos_degree: int = int(random.random() * 6)
        if (sin_degree == 0 and cos_degree == 0):
            return self._get_expression()

        x_coef: int = int(random.random() * 9 + 1)
        inner_part: str = Utils.combine_coef_var(x_coef, "x")
        return f"""
{Utils.raise_trig_power("sin", inner_part, sin_degree)}
<mo>&InvisibleTimes;</mo>
{Utils.raise_trig_power("cos", inner_part, cos_degree)}
"""