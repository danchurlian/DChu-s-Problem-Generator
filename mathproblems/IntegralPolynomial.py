from .Utils import Utils

class IntegralPolynomial(object):
    def __init__(self, degree: int):
        self.degree = degree
        pass

    def get_mathml(self) -> str:
        expression: str = Utils.polynomial(self.degree)

        return f"""
<div>Evaluate the integral below.</div>
<div>Make sure to add + C!</div>

<math>
    <mo>&int;</mo>
    <mo>(</mo>
        {expression}
    <mo>)</mo>
    <mi>d</mi>
    <mi>x</mi>
</math>

"""