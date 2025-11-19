from .Problem import Problem
import random

class BSTProblem(Problem):
    def __init__(self):
        super().__init__()

    def _get_problem_str(self) -> str:
        list = [i for i in range(1, 10)]
        result = "Please draw the following Binary Search Tree: "

        random.shuffle(list)
        for n in list:
            result += f"{n} "
        
        return result.rstrip()