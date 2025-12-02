from .Problem import Problem
import random
import math

class HeapProblem(Problem):
    def __init__(self):
        self.heaparr = self._init_heaparr()
        super().__init__()
    
    # Initializes the heap array
    def _init_heaparr(self):
        arr = []
        for i in range(8):
            ran = math.floor(random.random() * 30 + 1)
            HeapProblem._add_to_heap(arr, ran)
        return arr
    
    # Adds numbers to the array in a min-heap fashion
    def _add_to_heap(arr, num: int):
        arr.append(num)

        curr_idx = len(arr) - 1
        parent_idx = math.floor((curr_idx - 1) / 2)

        while curr_idx != 0 and arr[curr_idx] < arr[parent_idx]:
            temp = arr[curr_idx]
            arr[curr_idx] = arr[parent_idx];
            arr[parent_idx] = temp 
            
            curr_idx = parent_idx
            parent_idx = math.floor((parent_idx - 1) / 2)

    # Displays the heap array and instructions.
    def _get_problem_str(self):
        result = "The min-heap has been initialized as follows:\n"
        for n in self.heaparr:
            result += str(n) + " "
        result += f"""\nDo the following instructions:
- Please get the smallest element and remove it from the heap. Write down the result."""
        for i in range(3):
            ran_insert = int(random.random() * 20 + 1)
            result += f"""
- Please insert {ran_insert}. Write down the resulting heap."""
        return result