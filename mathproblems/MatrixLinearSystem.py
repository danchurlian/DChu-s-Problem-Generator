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
        column_specs: str = ""
        for i in range(len(self.sols)):
            matrix_str += self._new_equation()
        for i in range(self.dimension):
            if (i == self.dimension - 1):
                column_specs += "solid"
            else:
                column_specs += "none "
        column_specs = column_specs.strip()

        result: str = f"""
<div>Given this augmented matrix, solve the following linear system below.</div>
<div>
    <math>
        <mrow>
            <mo>[</mo>
            <mtable columnlines="{column_specs}">
                {matrix_str}
            </mtable>
            <mo>]</mo>
        </mrow>
    </math>
</div>
"""
        return result