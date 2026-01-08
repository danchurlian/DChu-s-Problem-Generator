from .IntegralProblem import IntegralProblem
import random
class IntegralTrigSub(IntegralProblem):
    def __init__(self):
        super().__init__()

    def _get_expression(self):
        a: int = int(random.random() * 5 + 1)
        operator: str = random.choice(["+", "-"]) 
        return f"""
<msqrt>
    <mn>{a ** 2}</mn>
    <mo>{operator}</mo>
    <msup>
        <mi>x</mi>
        <mn>2</mn>
    </msup>
</msqrt>
"""
        