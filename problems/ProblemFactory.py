from .Problem import Problem
from .BSTProblem import BSTProblem
from .HeapProblem import HeapProblem
from .ArraySortingProblem import ArraySortingProblem
from .NumberConversionProblem import NumberConversionProblem
from .TwoComplement import TwoComplement
from .BitwiseProblem import BitwiseProblem
from .HexaBitwise import HexaBitwise
from .AsciiConversionProblem import AsciiConversionProblem
from .ArrayGenerator import ArrayGenerator

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
                        errormsg += "Argument must be between 0 and 20! "
                except ValueError:
                    errormsg += "Argument was not an integer! "
                    pass
            else:
                errormsg += "Must have exactly one integer argument! "
            errormsg += "Type the command as shown below:\nsort 20"
                
        elif (problem_type in ["heap", "minheap"]):
            return HeapProblem()
        
        elif (problem_type in ["conv"]):
            if (args == None or len(args) == 0):
                return NumberConversionProblem(None)
            else:
                return NumberConversionProblem(args[0])

        elif (problem_type in ["twocomp"]):
            problem_type: str = "d"
            if (args is not None and len(args) == 1 and args[0] == "b"):
                problem_type: str = "b"
            return TwoComplement(problem_type)
        

        elif (problem_type in ["bitwise", "bit"]):
            return BitwiseProblem()
        

        elif (problem_type in ["hexabitwise", "hbit"]):
            num_problems: int = 10
            operator: str = None
            if (args is not None and len(args) >= 1):
                # Get the user argument for number of problems
                try:
                    arg_number: int = int(args[0])
                    if (arg_number < 1 or arg_number > 10):
                        raise ValueError()
                    else:
                        num_problems = arg_number
                except:
                    pass
                
                # Get the type of operator argument
                try:
                    operator_arg: str = args[1]
                    if (operator_arg not in ["and", "or"]):
                        raise ValueError()
                    else:
                        operator = operator_arg
                except:
                    pass

            return HexaBitwise(num_problems, operator)
            
        
        elif (problem_type in ["ascii"]):
            problem_type: str = "decode" 
            if (args is not None and len(args) == 1 and args[0] == "encode"):
                problem_type = "encode"
            return AsciiConversionProblem(problem_type)

        elif (problem_type in ["arrgen"]):
            errormsg = "ArrayGenerationError: "
            if (args != None and (len(args) == 3 or len(args) == 4)):
                try:
                    num_elts: int = int(args[0])
                    if (num_elts <= 0 or num_elts > 30):
                        raise ValueError()

                    low: int = int(args[1])
                    high: int = int(args[2])
                    allow_dupliates: bool = len(args) == 3 or args[3] != "false"
                    return ArrayGenerator(num_elts, low, high, allow_dupliates)
                except Exception:
                    pass
            errormsg += """You must have 3 to 4 arguments! Cannot generate more than 30 elements!
Example: arrgen 20 0 10 false"""
        
        return Problem(errormsg)