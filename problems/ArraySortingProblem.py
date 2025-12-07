from .Problem import Problem
import random, math

class ArraySortingProblem(Problem):
    def __init__(self, num_elts: int):
        self.num_elts = num_elts
        super().__init__()
    
    def _get_problem_str(self):
        result: str = "Here is an unsorted array of integers:\n["
        for i in range(self.num_elts):
            # generate a random number
            result += f"{math.floor(random.random() * 25 + 1)}"
            result += " " if (i != self.num_elts - 1) else "" 

        result += f"]\nSort the above list of numbers using:\nBubbleSort\nSelectionSort\nInsertionSort\nTreeSort(BST)\nHeapSort(Binary heap)"

        return result