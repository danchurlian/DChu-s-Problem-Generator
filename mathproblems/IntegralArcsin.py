from .IntegralProblem import IntegralProblem
import random

class IntegralArcsin(IntegralProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        random_negative: int = (-1) ** int(random.random() * 2)
        a: int = int(random.random() * 5 + 1)
        a_multiple: int = int(random.random() * 5 + 1)

        return f"""
<mfrac>
    <mn>{a_multiple * a * random_negative}</mn>
    <mrow>
        <msqrt>
            <mn>{a ** 2}</mn>
            <mo>-</mo>
            <msup>
                <mi>x</mi>
                <mn>2</mi>
            </msup>
        </msqrt>
    </mrow>
</mfrac>
"""