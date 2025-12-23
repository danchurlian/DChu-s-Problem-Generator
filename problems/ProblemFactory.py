from .Problem import Problem
from .BSTProblem import BSTProblem
from .MatrixLinearSystemProblem import MatrixLinearSystemProblem
from .LinearPlanarSystemProblem import LinearPlanarSystemProblem
from .HeapProblem import HeapProblem
from .ArithmeticProblem import ArithmeticProblem
from .ArraySortingProblem import ArraySortingProblem
from .NumberConversionProblem import NumberConversionProblem

class ProblemFactory(object):
    def __init__(self):
        pass

    def createProblem(problem_type: str, args: list = None) -> Problem:
        errormsg: str = "Invalid command!\n"
        if (problem_type in ["bst", "bstdraw", "bstproblem"]):
            return BSTProblem()

        # elif (problem_type in ["diffsys", "planarsys", "psys"]):
        #     return LinearPlanarSystemProblem()
        
        # elif (problem_type == "matsys"):
        #     errormsg = "MatsysError: "
        #     if (args and len(args) == 1):
        #         try:
        #             dimension = int(args[0])
        #             print(dimension)
        #             if (1 <= dimension and dimension <= 5):
        #                 return MatrixLinearSystemProblem(dimension)
        #             else:
        #                 errormsg += "Argument must be between 1 and 5 inclusive"
        #         except ValueError:
        #             errormsg += "Argument must be an integer greater than 0"
        #             pass
        #     else:
        #         errormsg += "Missing integer argument between 1 and 5 inclusive"

        # elif (problem_type in ["arith", "arithmetic"]):
        #     errormsg = "ArthmeticError: "
        #     if (args and len(args) == 1):
        #         try:
        #             print(args)
        #             num_probs = int(args[0])
        #             if (1 <= num_probs and num_probs <= 20):
        #                 return ArithmeticProblem(num_probs)
        #             else:
        #                 errormsg += "Argument must be between 1 and 20 inclusive"
        #         except ValueError:
        #             errormsg += "Argument must be an integer between 1 and 20 inclusive"
        #             pass
        #     else:
        #         errormsg += "Missing integer argument between 0 and 20 inclusive"
        
        elif (problem_type in ["sort", "sorting"]):
            errormsg = "SortingError: "
            if (args and len(args) == 1):
                try:
                    num_elts = int(args[0])
                    if (0 <= num_elts and num_elts <= 20):
                        return ArraySortingProblem(num_elts)
                    else:
                        errormsg += "Argument must be between 0 and 20 inclusive"
                except ValueError:
                    errormsg += "Argument must be an integer greater than 0"
                    pass
            else:
                errormsg += "Missing integer argument between 0 and 20 inclusive"
                
        elif (problem_type in ["heap", "minheap"]):
            return HeapProblem()
        
        elif (problem_type in ["conv"]):
            if (args == None or len(args) == 0):
                return NumberConversionProblem(None)
            else:
                return NumberConversionProblem(args[0])
        
        return Problem(errormsg)