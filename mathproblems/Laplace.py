from .MathProblem import MathProblem
from .Utils import Utils
import random


def new_exponential() -> str:
    coef: int = int(random.random() * 4 + 2)
    return f"""
<mn>{coef}</mn>
<mo>&InvisibleTimes;</mo>
<msup>
    <mi>e</mi>
    <mrow>
        {Utils.polynomial_new_term(1, "t", True)}
    </mrow>
</msup>
"""

def new_trig() -> str:
    coef: int = int(random.random() * 4 + 2)
    return f"""
<mn>{coef}</mn>
<mo>&InvisibleTimes;</mo>
{Utils.raise_trig_power("sin", Utils.polynomial_new_term(1, "t", True), 1)}
"""


class Laplace(MathProblem):
    def __init__(self, num_terms=1):
        super().__init__()
        self.num_terms = num_terms
    
    def get_mathml(self):
        rest_str: str = ""
        for i in range(self.num_terms - 1):
            chosen_func: function = random.choice([new_exponential, new_trig])
            rest_str += f"""
<mo>+</mo>
{chosen_func()}
"""

        return f"""
<div>Apply the laplace transform on the following expression.</div>
<math>
    <mrow>
        {new_exponential()}
        {rest_str}
    </mrow>
</math>
"""