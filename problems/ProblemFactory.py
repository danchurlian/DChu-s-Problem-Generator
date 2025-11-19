from .Problem import Problem
from .BSTProblem import BSTProblem

class ProblemFactory(object):
    def __init__(self):
        pass

    def createProblem(problem_type: str) -> Problem:
        if (problem_type == "BSTProblem"):
            return BSTProblem()
        return Problem()