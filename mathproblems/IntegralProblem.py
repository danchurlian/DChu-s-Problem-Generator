from .MathProblem import MathProblem
class IntegralProblem(MathProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        pass

    def get_mathml(self):
        return f"""
<div>Evaluate the integral below.</div>
<div>Make sure to add + C!</div>
<div>
    <math>
        <mo>&int;</mo>
        <mo>(</mo>
            {self._get_expression()}
        <mo>)</mo>
        <mi>d</mi>
        <mi>x</mi>
    </math>
</div>
"""