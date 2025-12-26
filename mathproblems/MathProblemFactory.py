from .DerivativePolynomial import DerivativePolynomial
from .IntegralPolynomial import IntegralPolynomial
from .RootExpansion import RootExpansion
from .ArithmeticProblem import ArithmeticProblem
from .MatrixLinearSystem import MatrixLinearSystem
from .LinearPlanarSystem import LinearPlanarSystem
from .DiffEqSecondOrder import DiffEqSecondOrder

class MathProblemFactory(object):
    def create_problem_output(command: str, args: list[str]) -> str:
        output: str = "Invalid command!"
        if (command in ["arith"]):
            try:
                num_probs = int(args[0])
                if (num_probs < 1 or num_probs > 8):
                    raise ValueError()
                problem = ArithmeticProblem(num_probs) 
                output = problem.get_mathml()
            except Exception:
                output = "Argument must be a single integer between 1 and 8!"

        elif (command in ["matsys"]):
            try:
                dimension: int = int(args[0])
                if (dimension < 2 or dimension > 5):
                    raise ValueError()
                problem = MatrixLinearSystem(dimension)
                output = problem.get_mathml()
            except Exception as e:
                output = "Argument must be an integer between 2 and 5!"
        
        elif (command in ["psys"]):
            problem = LinearPlanarSystem()
            output = problem.get_mathml()

        elif (command in ["expand"]):
            try:
                num_roots = int(args[0])
                if (num_roots < 2 or num_roots > 5):
                    raise ValueError()
                problem = RootExpansion(num_roots)
                output = problem.get_mathml()
            except TypeError as te:
                output = "Must include a single argument that is an integer!"
            except IndexError as ie:
                output = "Only one argument is needed!"
            except ValueError as ve:
                output = "Argument must be an integer between 2 and 5!"
        elif (command in ["derive"]):
            try:
                degree: int = int(args[0])
                if (degree < 1 or degree > 5):
                    raise ValueError()
                problem = DerivativePolynomial(degree)
                output = problem.get_mathml()
            except Exception:
                output = "There must be exactly one argument that is an integer between 1 and 5!"
        
        elif (command in ["int"]):
            try:
                degree: int = int(args[0])
                if (degree < 1 or degree > 5):
                    raise ValueError()
                problem = IntegralPolynomial(degree)
                output = problem.get_mathml()
            except Exception:
                output = "There must be exactly one argument that is an integer between 1 and 5!"
        elif (command in ["diffeq"]):
            problem = DiffEqSecondOrder()
            output = problem.get_mathml()

        return output
        