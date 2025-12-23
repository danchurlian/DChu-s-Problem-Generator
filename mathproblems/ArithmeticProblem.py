import random,math

# MathML string
def _new_problem(prob_num: int) -> str:
    ops = ["+", "&divide;", "&times;"]
    ran1 = math.floor(random.random() * 10)
    ran2 = math.floor(random.random() * 10)

    if (ran2 != 0):
        ops.append('/')

    chosen_op = random.choice(ops)
    if (chosen_op == '&divide;'):
        ran1 = ran1 * ran2

    return f"""
<div>
{prob_num}) 
    <math>
        <mn>{ran1}</mn>
        <mo>{chosen_op}</mo>
        <mn>{ran2}</mn> 
        <mo>=</mo>
    </math>
</div>
"""

class ArithmeticProblem(object):
    def __init__(self, num_probs: int):
        self.num_probs = num_probs

    def get_mathml(self):
        result: str = ""
        for i in range(self.num_probs):
            result += _new_problem(i+1)
        return result