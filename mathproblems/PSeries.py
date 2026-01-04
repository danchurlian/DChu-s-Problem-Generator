from .SeriesProblem import SeriesProblem
from .Utils import Utils
import random

class PSeries(SeriesProblem):
    def __init__(self):
        super().__init__()
    
    def _get_expression(self):
        deg: int = int(random.random() * 5 + 1)        
        return f"""
        <mfrac>
            <mn>1</mn>
            {Utils.raise_power("<mi>n</mi>", deg, "times")}
        </mfrac>
"""