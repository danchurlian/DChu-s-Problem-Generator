from .Problem import Problem
from .BSTProblem import BSTProblem
from .MatrixLinearSystemProblem import MatrixLinearSystemProblem

class ProblemFactory(object):
    def __init__(self):
        pass

    def createProblem(problem_type: str, args: list = None) -> Problem:
        if (problem_type == "bstdraw" or problem_type == "bstproblem"):
            return BSTProblem()
        elif (problem_type == "matsys"):
            return MatrixLinearSystemProblem()
        return Problem()