from .DerivativePolynomial import DerivativePolynomial
from .IntegralPolynomial import IntegralPolynomial
from .IntegralArctan import IntegralArctan
from .IntegralArcsin import IntegralArcsin
from .RootExpansion import RootExpansion
from .ArithmeticProblem import ArithmeticProblem
from .MatrixLinearSystem import MatrixLinearSystem
from .LinearPlanarSystem import LinearPlanarSystem
from .DiffEqSecondOrder import DiffEqSecondOrder
from .DiffEqAutonomous import DiffEqAutonomous

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
            if len(args) > 0:
                integralType: str = args[0]
                if (integralType == "poly"):
                    try:
                        degree: int = int(args[1])
                        if (degree < 1 or degree > 5):
                            raise ValueError()
                        problem = IntegralPolynomial(degree)
                        output = problem.get_mathml()
                    except Exception:
                        output = "Integral Polynomial syntax error: There must be exactly one argument that is an integer between 1 and 5!"
                elif (integralType in ["arctan", "invtan"]):
                    problem = IntegralArctan()
                    output = problem.get_mathml()
                elif (integralType in ["arcsin", "invsin"]):
                    problem = IntegralArcsin()
                    output = problem.get_mathml()
            else:
                output = "Integral no arguments!"

        elif (command in ["odeauto"]):
            num_stationary_points: int = 2
            try:
                if (len(args) == 1):
                    num_stationary_points: int = int(args[0])
                if (0 < num_stationary_points and num_stationary_points <= 4):
                    problem = DiffEqAutonomous(num_stationary_points)
                    output = problem.get_mathml()
                else:
                    raise ValueError()
            except Exception as e:
                output = "Argument must be a number between 1 and 4 inclusive!"
                
        elif (command in ["ode2"]):
            problem = DiffEqSecondOrder()
            output = problem.get_mathml()

        return output
        