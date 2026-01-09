from .DerivativePolynomial import DerivativePolynomial
from .IntegralPolynomial import IntegralPolynomial
from .IntegralArctan import IntegralArctan
from .IntegralArcsin import IntegralArcsin
from .IntegralSincos import IntegralSincos
from .IntegralSectan import IntegralSectan
from .IntegralTrigSub import IntegralTrigSub
from .IntegralByParts1 import IntegralByParts1
from .PartialFraction import PartialFraction
from .PSeries import PSeries
from .SeriesDirectComparison import SeriesDirectComparison
from .SeriesRational import SeriesRational
from .RootExpansion import RootExpansion
from .ArithmeticProblem import ArithmeticProblem
from .MatrixMultiply import MatrixMultiply
from .MatrixLinearSystem import MatrixLinearSystem
from .LinearPlanarSystem import LinearPlanarSystem
from .DiffEqSecondOrder import DiffEqSecondOrder
from .DiffEqAutonomous import DiffEqAutonomous

class MathProblemFactory(object):
    def create_problem_output(command: str, args: list[str]) -> str:
        output: str = "Invalid command!"
        problem = None

        if (command in ["arith"]):
            try:
                num_probs = int(args[0])
                if (num_probs < 1 or num_probs > 8):
                    raise ValueError()
                problem = ArithmeticProblem(num_probs) 
            except Exception:
                output = "Argument must be a single integer between 1 and 8!"

        elif (command in ["matmul"]):
            problem = MatrixMultiply()

        elif (command in ["matsys"]):
            try:
                dimension: int = int(args[0])
                if (dimension < 2 or dimension > 5):
                    raise ValueError()
                problem = MatrixLinearSystem(dimension)
            except Exception as e:
                output = "Argument must be an integer between 2 and 5!"
        
        elif (command in ["psys"]):
            problem = LinearPlanarSystem()

        elif (command in ["expand"]):
            try:
                num_roots = int(args[0])
                if (num_roots < 2 or num_roots > 5):
                    raise ValueError()
                problem = RootExpansion(num_roots)
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
                    except Exception:
                        output = "Integral Polynomial syntax error: There must be exactly one argument that is an integer between 1 and 5!"
                elif (integralType in ["arctan", "invtan"]):
                    problem = IntegralArctan()
                elif (integralType in ["arcsin", "invsin"]):
                    problem = IntegralArcsin()
                elif (integralType in ["sincos"]):
                    problem = IntegralSincos()
                elif (integralType in ["sectan"]):
                    problem = IntegralSectan()
                elif (integralType == "trigsub"):
                    problem = IntegralTrigSub()
                elif (integralType == "ibp1"):
                    problem = IntegralByParts1()
            else:
                output = "You must specify the type of integral to generate!  Ex: 'int sincos'"
        elif (command == "pfrac"):
            problem = PartialFraction()
        elif (command == "pseries"):
            problem = PSeries()
        elif (command == "dct"):
            problem = SeriesDirectComparison()
        elif (command == "rationalseries"):
            problem = SeriesRational()
        elif (command in ["odeauto"]):
            num_stationary_points: int = 2
            try:
                if (len(args) == 1):
                    num_stationary_points: int = int(args[0])
                if (0 < num_stationary_points and num_stationary_points <= 4):
                    problem = DiffEqAutonomous(num_stationary_points)
                else:
                    raise ValueError()
            except Exception as e:
                output = "Argument must be a number between 1 and 4 inclusive!"
                
        elif (command in ["ode2"]):
            problem = DiffEqSecondOrder()
        
        if (problem != None):
            output = problem.get_mathml()

        return output
        