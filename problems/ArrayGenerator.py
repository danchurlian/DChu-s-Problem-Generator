from .Problem import Problem
import random

def _new_array(num_elts: int, low: int, high: int, allow_duplicates: bool) -> list:
    result = None
    if (allow_duplicates):
        # Create a list of randomly generated numbers
        result = list()
        for i in range(num_elts):
            new_num: int = int(random.random() * (high-low+1) + low)
            result.append(new_num)
    else:
        # Use a set to record the generated numbers (which uses hashing is more efficient)
        unique_set = set()
        while (len(unique_set) < num_elts):
            new_num: int = int(random.random() * (high-low+1) + low)
            unique_set.add(new_num)
            # stop when range is too small for length, when len = range inclusive
            if (len(unique_set) == (high-low+1)):
                break
        result = [n for n in unique_set]
        random.shuffle(result)
    return result 

class ArrayGenerator(Problem):
    def __init__(self, num_elts: int, low: int, high: int, allow_duplicates: bool = True):
        self.num_elts = num_elts
        self.low = low
        self.high = high
        self.allow_duplicates = allow_duplicates
        super().__init__()

    def _get_problem_str(self):
        return str(_new_array(self.num_elts, self.low, self.high, self.allow_duplicates))