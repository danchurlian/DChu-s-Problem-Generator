from .Utils import Utils
from .MathProblem import MathProblem
from .IntegralProblem import IntegralProblem

class IntegralPolynomial(IntegralProblem):
    def __init__(self, degree: int):
        super().__init__()
        self.degree = degree
    
    def _get_expression(self):
        return Utils.polynomial(self.degree)

#     def get_mathml(self) -> str:
#         expression: str = Utils.polynomial(self.degree)
#         expression = inverseTangent()
#         return f"""
# <div>Evaluate the integral below.</div>
# <div>Make sure to add + C!</div>
# <div>
#     <math>
#         <mo>&int;</mo>
#         <mo>(</mo>
#             {expression}
#         <mo>)</mo>
#         <mi>d</mi>
#         <mi>x</mi>
#     </math>
# </div>
# """