from .IntegralProblem import IntegralProblem
from .Utils import Utils
import random

class IntegralSectan(IntegralProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        sec_degree: int = int(random.random() * 6)
        tan_degree: int = int(random.random() * 6)
        if (sec_degree == 0 and tan_degree == 0):
            return self._get_expression()

        x_coef: int = int(random.random() * 9 + 1)
        inner_part: str = Utils.combine_coef_var(x_coef, "x")
        return f"""
{Utils.raise_trig_power("sec", inner_part, sec_degree)}
<mo>&InvisibleTimes;</mo>
{Utils.raise_trig_power("tan", inner_part, tan_degree)}
"""