import random

class DerivativePolynomial(object):
    def __init__(self):
        self.degree = 2
        pass

    # MathML string
    def new_term(self, exponent: int) -> str:
        result: str = ""
        coef: int = int(random.random() * 13 - 6)
        if (coef != 0):
            if (abs(coef) == 1):
                if (coef < 0):
                    result += f"<mo>-</mo>"
            else:
                if (coef < 0):
                    result = f"<mo>-</mo><mn>{-coef}</mn>"
                else:
                    result += f"<mo>+</mo><mn>{coef}</mn>"

            exponential: str = ""
            if (exponent > 1):
                exponential = f"<msup><mi>x</mi><mn>{exponent}</mn></msup>" 
            elif (exponent == 1):
                exponential = f"<mi>x</mi>"
            else:
                exponential = f"<mn>1</mn>"
            result += exponential

        return result
    
    # def get_polynomial(self) -> str:


    def get_mathml(self):
        expression: str = ""
        for i in range(self.degree, -1, -1):
            expression += self.new_term(i) 
        return f"""
<math>
    {expression}
</math>
"""
    
