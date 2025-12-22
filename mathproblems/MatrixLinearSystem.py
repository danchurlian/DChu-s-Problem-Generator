import random, math

class MatrixLinearSystem(object):
    def __init__(self, dimension:int = 3):
        self.dimension = dimension
        self.sols = self._generate_solution()


    def _generate_solution(self):
        sols = []
        for i in range(self.dimension):
            while (True):
                ran = int(random.random() * 9 - 4)
                if not ran in sols:
                    sols.append(ran) 
                    break
        return sols
    

    def _new_equation(self) -> str:
        sum: int = 0
        result: str = "<mtr>"
        for component in self.sols:
            coef: int = int(random.random() * 13 - 6)
            term = coef * component
            sum += term
            result += f"<mtd><mn>{coef:3d}</mn></mtd>\n"
        result += f"<mtd><mn>{sum:3d}</mn></mtd>\n</mtr>\n"
        return result
    

    def get_mathml(self) -> str:
        matrix_str: str = ""
        for i in range(len(self.sols)):
            matrix_str += self._new_equation()
        result: str = f"""
<div>Given this augmented matrix, solve the following linear system below.</div>
</br>
<math>
    <mrow>
        <mo>[</mo>
        <mtable columnlines="none none solid">
            {matrix_str}
        </mtable>
        <mo>]</mo>
    </mrow>
</math>
"""
        return result