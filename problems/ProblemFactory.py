from .Problem import Problem
from .BSTProblem import BSTProblem
from .MatrixLinearSystemProblem import MatrixLinearSystemProblem
from .LinearPlanarSystemProblem import LinearPlanarSystemProblem
from .HeapProblem import HeapProblem
from .ArithmeticProblem import ArithmeticProblem
from .ArraySortingProblem import ArraySortingProblem

class ProblemFactory(object):
    def __init__(self):
        pass

    def createProblem(problem_type: str, args: list = None) -> Problem:
        if (problem_type in ["bst", "bstdraw", "bstproblem"]):
            return BSTProblem()

        # elif (problem_type in ["diffsys", "planarsys", "psys"]):
        #     return LinearPlanarSystemProblem()
        
        elif (problem_type == "matsys"):
            if (args and len(args) == 1):
                try:
                    dimension = int(args[0])
                    return MatrixLinearSystemProblem(dimension if 0 < dimension and dimension <= 5 else 3)
                except ValueError:
                    pass
            return MatrixLinearSystemProblem()

        elif (problem_type in ["arith", "arithmetic"]):
            if (args and len(args) == 1):
                try:
                    print(args)
                    num_probs = int(args[0])
                    if (0 <= num_probs and num_probs <= 20):
                        return ArithmeticProblem(num_probs)
                except ValueError:
                    pass
        
        elif (problem_type in ["sort", "sorting"]):
            if (args and len(args) == 1):
                try:
                    num_elts = int(args[0])
                    if (0 <= num_elts and num_elts <= 20):
                        return ArraySortingProblem(num_elts)
                except ValueError:
                    pass
                
        elif (problem_type in ["heap", "minheap"]):
            return HeapProblem()
        
        return Problem()