from .Problem import Problem
import random

class BinaryProblem(Problem):
    def __init__(self):
        super().__init__()
    
    def _get_problem_str(self):
        nums = []
        for i in range(5):
            nums.append(int(random.random() * 256))
        result: str = f"The list of numbers are: {nums}.\nWrite those numbers in binary."
        return result 