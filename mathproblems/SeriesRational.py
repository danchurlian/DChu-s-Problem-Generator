from .SeriesProblem import SeriesProblem
from .Utils import Utils
import random

class SeriesRational(SeriesProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        # top and bottom 1 to 5
        top_degree: int = int(random.random() * 4)
        bottom_degree: int = int(random.random() * 5 + 1)
        return f"""
<mfrac>
    {Utils.polynomial(top_degree, "n")}
    {Utils.polynomial(bottom_degree, "n")}
</mfrac>
"""