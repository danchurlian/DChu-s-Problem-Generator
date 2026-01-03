from .IntegralProblem import IntegralProblem
import random

class IntegralArctan(IntegralProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        # b * dx / (a^2 + x^2)
        a: int = int(random.random() * 5 + 1)
        a_multiple: int = int(random.random() * 5 + 1)

        a_factors: list = []
        for i in range(2,a+1):
            if (a % i == 0):
                a_factors.append(i)
        # 4 -> 1 2 4 -> list of factors, randomly select -> coefficient of dx
        b: int = (random.choice(a_factors)) if len(a_factors) > 0 else 1
        print(f"a {a} b {b}")
        return f"""
<mfrac>
    <mrow>
        <mn>{a_multiple * a}</mn>
    </mrow>
    <mrow>
        <mn>{a**2}</mn>
        <mo>+</mo>
        <msup>
            <mi>x</mi>
            <mn>2</mn>
        </msup>
    </mrow>
</mfrac>
"""