from .Problem import Problem
from enum import Enum, auto
import random

# CONSTANTS
ARR_SIZE: int = 8
NUM_QUESTIONS: int = 6

# These are the different types of questions, which affect what
# goes into the index expression inside the square brackets.
class _QuestionType(Enum):
    CONST_LEFT = auto()
    CONST_RIGHT = auto()
    I_LEFT = auto()
    I_RIGHT = auto()
    DOUBLE_CONST = auto()
    DOUBLE_I = auto()
    COMPLEMENT_I = auto()
    OFFSET_LEFT = auto()
    OFFSET_RIGHT = auto()

# Returns a random string containing the index expression that is supposed
# to be nested in square brackets.
def random_index() -> str:
    question_type: _QuestionType = random.choice(list(_QuestionType))
    result: str = "unknown index"
    random_const: int = random.randint(0, ARR_SIZE - 1)
    match question_type:
        case _QuestionType.CONST_LEFT:
            result = str(random_const)
        case _QuestionType.CONST_RIGHT:
            result = f"len - {random_const}"
        case _QuestionType.I_LEFT:
            result = "i"
        case _QuestionType.I_RIGHT:
            result = "len - i"
        case _QuestionType.DOUBLE_CONST:
            random_const = random.randint(0, (ARR_SIZE // 2) - 1) 
            result = f"{random_const} * 2"
        case _QuestionType.DOUBLE_I:
            result = "i * 2"
        case _QuestionType.COMPLEMENT_I:
            result = "complement of i"
        case _QuestionType.OFFSET_LEFT:
            random_const = random.randint(0, (ARR_SIZE // 2) - 1) 
            result = f"i + {random_const}" 
        case _QuestionType.OFFSET_RIGHT:
            random_const = random.randint(0, (ARR_SIZE // 2) - 1) 
            result = f"len - i - {random_const}"

    return result


# Returns an array full of between 0-9 an in array of size ARR_SIZE.
def get_random_array() -> list:
    return [ random.randint(0, 9) for i in range(ARR_SIZE) ]

# Returns a random value for the i variable in the problem.
def random_i() -> int:
    return random.randint(0, ARR_SIZE // 2 - 1)


class ArrayIndexProblem(Problem):
    def __init__(self):
        super().__init__()

    def _get_problem_str(self):
        arr: list = get_random_array()

        # The introduction to the problems and variable information
        result: str = f"""Here is an array: {arr}
Let i = {random_i()}.
Let 'len' be the length of the array.
Let 'complement' be the index when i is reflected horizontally.

Solve the following questions on a piece of paper. Even better,
try to visualize the index and the position the answer would be
in your head.

Note that some indices may be out of bounds.\n"""
        # Generate NUM_QUESTIONS lines of questions.
        for i in range(NUM_QUESTIONS):
            line: str = f"{i + 1}. What is the value of arr[{random_index()}]?\n"
            result += line
        return result