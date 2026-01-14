from .DerivativePolynomial import DerivativePolynomial
from .IntegralPolynomial import IntegralPolynomial
from .IntegralArctan import IntegralArctan
from .IntegralArcsin import IntegralArcsin
from .IntegralSincos import IntegralSincos
from .IntegralSectan import IntegralSectan
from .IntegralTrigSub import IntegralTrigSub
from .IntegralByParts1 import IntegralByParts1
from .Laplace import Laplace
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
                output = """
                <div>Argument must be a single integer between 1 and 8!</div>
                <div>Example: 'arith 8'</div>
                """

        elif (command in ["matmul"]):
            problem = MatrixMultiply()

        elif (command in ["matsys"]):
            try:
                dimension: int = int(args[0])
                if (dimension < 2 or dimension > 5):
                    raise ValueError()
                problem = MatrixLinearSystem(dimension)
            except Exception:
                output = """<div>Argument must be an integer between 2 and 5!</div>
                <div>Example: 'matsys 3'</div>"""
        
        elif (command in ["psys"]):
            problem = LinearPlanarSystem()

        elif (command in ["expand"]):
            try:
                num_roots = int(args[0])
                if (num_roots < 2 or num_roots > 5):
                    raise ValueError()
                problem = RootExpansion(num_roots)
            except Exception:
                output = """<div>Must have an integer argument between 2 and 5!</div>
                <div>Example: 'expand 2'</div>"""
        elif (command in ["derive"]):
            try:
                degree: int = int(args[0])
                if (degree < 1 or degree > 5):
                    raise ValueError()
                problem = DerivativePolynomial(degree)
            except Exception:
                output = """<div>There must be exactly one argument that is an integer between 1 and 5!</div>
                <div>Example: 'derive 2'</div>"""
        
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
                        output = """<div>There must be exactly one argument that is an integer between 1 and 5!</div>
                        <div>Example: 'int poly 1'</div>"""
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
                    output = """<div>Invalid type of integral problem! Try one of the following and refer to the table:</div>
                    <div>'int sincos'</div>
                    <div>'int invsin'</div>"""
            else:
                output = """<div>You must specify the type of integral to generate!</div>
                <div>Example: 'int sincos'</div>"""
        elif (command == "laplace"):
            try:
                num_terms: int = int(args[0])
                if (num_terms > 5):
                    raise ValueError()
                problem = Laplace(num_terms)
            except Exception:
                output = """<div>You must specify one argument that is an integer and not more than 5!</div>
                <div>Example: laplace 3</div>"""
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
            except Exception:
                output = """<div>Argument must be a number between 1 and 4 inclusive!</div>
                <div>Example: 'odeauto 1'</div>"""
                
        elif (command in ["ode2"]):
            problem = DiffEqSecondOrder()
        
        if (problem != None):
            output = problem.get_mathml()

        return output
        