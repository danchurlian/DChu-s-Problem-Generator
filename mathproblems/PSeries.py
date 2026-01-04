from .MathProblem import MathProblem
from .Utils import Utils
import random

class PSeries(MathProblem):
    def __init__(self):
        super().__init__()
    
    def get_mathml(self):
        deg: int = int(random.random() * 5 + 1)        
        return f"""
<div>Does the following converge or diverge?</div>
<math>
    <mrow>
        <munderover>
            <mo>&sum;</mo>
            <mrow>
                <mi>n</mn>
                <mo>=</mo>
                <mn>1</mn>
            </mrow>
            <mo>∞</mo>
        </munderover>
        <mfrac>
            <mn>1</mn>
            {Utils.raise_power("<mi>n</mi>", deg, "times")}
        </mfrac>
    </mrow>
</math>
"""