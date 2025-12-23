from .Utils import Utils
import random

class DerivativePolynomial(object):
    def __init__(self, degree: int):
        self.degree = degree
        pass

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
    
