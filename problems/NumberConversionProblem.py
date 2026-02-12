from .Problem import Problem
from .NumberConversionHandler import NumberConversionHandler
import random


class NumberConversionProblem(Problem):
    # Options can be b2d, d2b
    def __init__(self, option: str):
        self.option = option
        super().__init__()

    def decimal_prob(self):
        nums = []
        for i in range(5):
            nums.append(int(random.random() * 256))
        result: str = f"The list of decimal numbers are: {nums}.\nWrite those numbers in binary.\nWrite those numbers in octal.\nWrite those numbers in hexadecimal."
        return result 
    
    def binary_prob(self):
        nums = []
        for i in range(5):
            random_num: int = int(random.random() * 256)
            nums.append(NumberConversionHandler.decimal_to_binary(random_num))
        result: str = f"The list of binary numbers are: {nums}.\nWrite those numbers in hexadecimal.\nWrite those numbers in octal.\nWrite those numbers in decimal."
        return result
    
    def octal_prob(self) -> str:
        nums_str: list[str] = []
        for i in range(5):
            digit1: int = random.randint(0, 3)
            digit2: int = random.randint(0, 7)
            digit3: int = random.randint(0, 7)
            curr_num_str: str = str(digit1) + str(digit2) + str(digit3)
            nums_str.append(curr_num_str)
        result: str = f"The list of octal numbers are: {nums_str}.\nWrite those numbers in binary.\nWrite those numbers in decimal.\nWrite those numbers in hexadecimal."
        return result
    
    def hex_prob(self):
        nums = []
        for i in range(5):
            random_num: int = int(random.random() * 256)
            nums.append(hex(random_num))
        result: str = f"The list of random hexadecimal numbers are: {nums}.\nWrite those numbers in binary.\nWrite those numbers in octal.\nWrite those numbers in decimal."
        return result 

    
    def _get_problem_str(self):
        if (self.option in ["b", "bin", "binary"]):
            return self.binary_prob()
        elif (self.option in ["d", "decimal"]):
            return self.decimal_prob()
        elif (self.option in ["o", "oct", "octal"]):
            return self.octal_prob()
        elif (self.option in ["h", "hex", "hexadecimal"]):
            return self.hex_prob()
        return f"Invalid argument for NumberConversionProblem command. Write the command as either the following:\nconv d\nconv b\nconv o\nconv h"