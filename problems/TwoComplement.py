from .Problem import Problem
from .NumberConversionHandler import NumberConversionHandler
import random

class TwoComplement(Problem):
    # problem_type can be either the following: "d" or "b"
    def __init__(self, problem_type: str):
        self.problem_type = problem_type
        super().__init__()

    def _get_problem_str(self) -> str:
        result: str = ""
        if (self.problem_type == "d"):
            # Random number generator
            num: int = random.randint(-128, -1)
            result = f"Write this number {num} in binary using 8-bit two's complement."
        
        elif (self.problem_type == "b"):
            # Generate a random number and convert it to binary to display to the output
            num: int = random.randint(128, 255)
            binary_str: str = NumberConversionHandler.decimal_to_binary(num)
            result = f"Write this negative signed binary number '{binary_str}' into decimal using two's complement."
            
        return result