from .Problem import Problem
from .BSTProblem import BSTProblem
from .MatrixLinearSystemProblem import MatrixLinearSystemProblem
from .HeapProblem import HeapProblem

class ProblemFactory(object):
    def __init__(self):
        pass

    def createProblem(problem_type: str, args: list = None) -> Problem:
        if (problem_type in ["bst", "bstdraw", "bstproblem"]):
            return BSTProblem()
        
        elif (problem_type == "matsys"):
            if (args and len(args) == 1):
                try:
                    dimension = int(args[0])
                    return MatrixLinearSystemProblem(dimension if 0 < dimension and dimension <= 5 else 3)
                except ValueError:
                    pass
            return MatrixLinearSystemProblem()
        elif (problem_type in ["heap", "minheap"]):
            return HeapProblem()
        return Problem()