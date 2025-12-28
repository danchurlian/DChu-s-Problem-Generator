from .Utils import Utils
from .MathProblem import MathProblem
import random

class DerivativePolynomial(MathProblem):
    def __init__(self, degree: int):
        super().__init__()
        self.degree = degree

    def get_mathml(self):
        expression: str = Utils.polynomial(self.degree)

        return f"""
<div>
    Write down the 1st derivative of the expression below.
</div>
<div>
    <math>
        <mfrac>
            <mrow><mi>d</mi></mrow>
            <mrow><mi>d</mi><mi>x</mi></mrow>
        </mfrac>
        <mo>(</mo>
            {expression}
        <mo>)</mo>
    </math>
</div>
"""
    
