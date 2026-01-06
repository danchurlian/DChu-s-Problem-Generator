from .MathProblem import MathProblem
import random

def _new_binomial():
    root: int = int(random.random() * 5 + 1)
    root *= (-1) ** int(random.random() * 2)
    second_part: str = ""
    if (root > 0):
        second_part = f"<mo>-</mo> <mn>{root}</mn>"
    elif (root < 0):
        second_part = f"<mo>+</mo> <mn>{-root}</mn>"

    return f"""
<mo>(</mo><mi>x</mi> {second_part}<mo>)</mo>
"""

class PartialFraction(MathProblem):
    def __init__(self):
        pass
    
    def get_mathml(self):
        numerator: int = int(random.random() * 5 + 1)
        random_neg: int = (-1) ** int(random.random() * 2)
        numerator *= random_neg

        return f"""
<div>Use partial fractions below.</div>
<math>
    <mrow>
        <mfrac>
            <mn>{numerator}</mn>
            <mrow>
                {_new_binomial()}
                {_new_binomial()}
            </mrow>
        </mfrac>
    </mrow>
</math>
"""

