from .Problem import Problem
import random

def random_binary() -> str:
    result: str = ""
    for i in range(8):
        result += str(random.randint(0,1)) 
    return result

class BitwiseProblem(Problem):
    def __init__(self):
        super().__init__()

    
    def _get_problem_str(self) -> str:
        # get two integers, convert them to binary. 
        return f"""Below are two 8-bit binary integers.
{random_binary()}
{random_binary()}

Perform a bitwise AND (&) operation with them.
Perform a bitwise OR (|) operation with them.

Write down the results on paper, and convert each of them 
to octal, decimal, and hexadecimal.
"""