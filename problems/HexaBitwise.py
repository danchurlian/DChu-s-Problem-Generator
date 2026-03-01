from .Problem import Problem
import random

ARG_TO_OPERATOR_SYMBOL: dict = {
    "and": "&",
    "or": "|",
}

# Return a random single hexadecimal digit
def random_hex():
    return hex(random.randint(0, 15)) 

# Return a random operator
def random_operator():
    operators: list = ["&", "|"]
    return random.choice(operators)

# Generate a line. 
def random_equation(chosen_operator: str) -> str:
    operator: str = (ARG_TO_OPERATOR_SYMBOL[chosen_operator] 
                    if chosen_operator is not None
                    else random_operator())
    return f"{random_hex()} {operator} {random_hex()} = "


class HexaBitwise(Problem):
    def __init__(self, num_problems: int, chosen_operator: str = None):
        self.num_problems = num_problems
        self.chosen_operator = chosen_operator
        super().__init__()

    def _get_problem_str(self):
        result: str = "Write the results of the bitwise operations on paper.\n" 
        for i in range(1, self.num_problems + 1):
            result += f"{i}. {random_equation(self.chosen_operator)}\n"
        return result