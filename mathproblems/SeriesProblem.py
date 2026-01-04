from .MathProblem import MathProblem

class SeriesProblem(MathProblem):
    def __init__(self):
        pass
    
    def _get_expression(self):
        raise NotImplementedError()

    def get_mathml(self):
        return f"""
<div>Does the following converge or diverge?</div>
<math>
    <mrow>
        <munderover>
            <mo>&sum;</mo>
            <mrow>
                <mi>n</mi>
                <mo>=</mo>
                <mn>1</mn>
            </mrow>
            <mo>∞</mo>
        </munderover>
        {self._get_expression()}
    </mrow>
</math>
"""