from .Problem import Problem
import random

# Return a random single hexadecimal digit
def random_hex():
    return hex(random.randint(0, 15)) 

# Return a random operator
def random_operator():
    operators: list = ["&", "|"]
    return random.choice(operators)

# Generate a line. 
def random_equation() -> str:
    return f"{random_hex()} {random_operator()} {random_hex()} = "

class HexaBitwise(Problem):
    def __init__(self, num_problems: int):
        self.num_problems = num_problems
        super().__init__()

    def _get_problem_str(self):
        result: str = "Write the results of the following bitwise operations on paper.\n" 
        for i in range(1, self.num_problems + 1):
            result += f"{i}. {random_equation()}\n"
        return result