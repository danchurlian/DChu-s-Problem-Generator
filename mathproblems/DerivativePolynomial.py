import random

class DerivativePolynomial(object):
    def __init__(self, degree: int):
        self.degree = degree
        pass

    # MathML string
    def new_term(self, exponent: int, start: bool) -> str:
        result: str = ""
        # coef should not be 0
        coef: int = int(random.random() * 13 - 6)
        while (coef == 0):
            coef = int(random.random() * 13 - 6)

        if (abs(coef) == 1):
            if (coef < 0):
                result += f"<mo>-</mo>"
            elif not start:
                result += f"<mo>+</mo>"
        else:
            if (coef < 0):
                result = f"<mo>-</mo><mn>{-coef}</mn>"
            else:
                if start:
                    result += f"<mn>{coef}</mn>" 
                else:
                    result += f"<mo>+</mo><mn>{coef}</mn>"

        exponential: str = ""
        if (exponent > 1):
            exponential = f"<msup><mi>x</mi><mn>{exponent}</mn></msup>" 
        elif (exponent == 1):
            exponential = f"<mi>x</mi>"
        elif (abs(coef) == 1):
            exponential = f"<mn>1</mn>"
        result += exponential

        return result
    

    def get_mathml(self):
        expression: str = ""
        for i in range(self.degree, -1, -1):
            expression += self.new_term(i, False) if i < self.degree else self.new_term(i, True)
        return f"""
<div>
    Write down the 1st derivative of the expression below.
</div>
<math>
    <mfrac>
        <mrow><mi>d</mi></mrow>
        <mrow><mi>d</mi><mi>x</mi></mrow>
    </mfrac>
    <mo>(</mo>
        {expression}
    <mo>)</mo>
</math>
"""
    
