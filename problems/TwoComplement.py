from .Problem import Problem
import random

class TwoComplement(Problem):
    def __init__(self):
        super().__init__()

    def _get_problem_str(self):
        # Random number generator
        num: int = random.randint(-128, -1)
        return f"Write this number {num} in binary using 8-bit two's complement."