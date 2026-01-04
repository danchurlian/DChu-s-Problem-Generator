from .SeriesProblem import SeriesProblem
from .Utils import Utils

class SeriesDirectComparison(SeriesProblem):
    def __init__(self):
        pass

    def _get_expression(self):
        return f""" 
        <mfrac>
            <mn>1</mn>
            <mrow>
                {Utils.polynomial(2, "n")}
            </mrow>
        </mfrac>
"""