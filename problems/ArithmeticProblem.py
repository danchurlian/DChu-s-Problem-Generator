from .Problem import Problem
import random
import math

class ArithmeticProblem(Problem):
    def __init__(self, num_probs):
        self.num_probs = num_probs
        super().__init__()
    
    def get_single_prob(self, prob_num) -> str:
        ops = ['+', '-', 'x']
        ran1 = math.floor(random.random() * 10)
        ran2 = math.floor(random.random() * 10)

        if (ran2 != 0):
            ops.append('/')

        chosen_op = random.choice(ops)
        if (chosen_op == '/'):
            ran1 = ran1 * ran2

        return f"{prob_num}) {ran1} {chosen_op} {ran2} = "
    
    def _get_problem_str(self):
        lines = ""
        for i in range(self.num_probs):
            lines += f"{self.get_single_prob(i + 1)}\n"
        return lines