from .Problem import Problem
import random

def _new_array(num_elts: int, low: int, high: int):
    result = list()
    for i in range(num_elts):
        new_num: int = int(random.random() * (high-low+1) + low)
        result.append(new_num)
    return result 

class ArrayGenerator(Problem):
    def __init__(self, num_elts: int, low: int, high: int):
        self.num_elts = num_elts
        self.low = low
        self.high = high
        super().__init__()

    def _get_problem_str(self):
        return str(_new_array(self.num_elts, self.low, self.high))