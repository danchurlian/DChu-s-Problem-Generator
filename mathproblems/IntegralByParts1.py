from .IntegralProblem import IntegralProblem
from .Utils import Utils
import random

class IntegralByParts1(IntegralProblem):
    def __init__(self):
        super().__init__()

    def _get_expression(self):
        return f"""
<msup>
    <mi>e</mi>
    <mrow>
        {Utils.polynomial_new_term(1, "x", True)}    
    </mrow>
</msup>
<mo>&InvisibleTimes;</mo>
<mi>{random.choice(["sin", "cos"])}</mi>
<mo>(</mo>
<mrow>
    {Utils.polynomial_new_term(1, "x", True)}
</mrow>
<mo>)</mo>
"""