from .MathProblem import MathProblem
from .Utils import Utils

class SeriesDirectComparison(MathProblem):
    def __init__(self):
        pass

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
        <mfrac>
            <mn>1</mn>
            <mrow>
                {Utils.polynomial(2, "n")}
            </mrow>
        </mfrac>
    </mrow>
</math>
"""