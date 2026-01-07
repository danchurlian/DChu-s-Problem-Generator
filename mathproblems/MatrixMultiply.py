from .MathProblem import MathProblem
import random

class MatrixMultiply(MathProblem):
    def __init__(self):
        super().__init__()

    def get_mathml(self):
        nums: list[int] = []
        for i in range(8):
            nums.append(int(random.random() * 11 - 5))
        
        return f"""
<div>Perform matrix multiplication on the following:</div>
<math>
    <mrow>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><mn>{nums[0]}</mn></mtd>
                <mtd><mn>{nums[1]}</mn></mtd>
            </mtr>
            <mtr>
                <mtd><mn>{nums[2]}</mn></mtd>
                <mtd><mn>{nums[3]}</mn></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
        <mo>[</mo>
        <mtable>
            <mtr>
                <mtd><mn>{nums[4]}</mn></mtd>
                <mtd><mn>{nums[5]}</mn></mtd>
            </mtr>
            <mtr>
                <mtd><mn>{nums[6]}</mn></mtd>
                <mtd><mn>{nums[7]}</mn></mtd>
            </mtr>
        </mtable>
        <mo>]</mo>
        <mo>=</mo>
    </mrow>
</math>
"""
        return super().get_mathml()