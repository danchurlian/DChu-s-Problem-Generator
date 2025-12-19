import random

def _new_binomial():
    root: int = int(random.random() * 13 - 6)
    second_part: str = ""
    if (root > 0):
        second_part = f"<mo>-</mo> <mn>{root}</mn>"
    elif (root < 0):
        second_part = f"<mo>+</mo> <mn>{-root}</mn>"

    return f"""
(<mi>x</mi> {second_part})
"""


class RootExpansion(object):
    def __init__(self, num_roots: int):
        self.num_roots = num_roots

    def get_mathml(self):
        expression: str = ""
        for i in range(self.num_roots):
            expression += _new_binomial()
        return f"""
<math>
    <mrow>
        {expression}
    </mrow>
</math>
"""