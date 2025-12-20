from .DerivativePolynomial import DerivativePolynomial
from .RootExpansion import RootExpansion

class MathProblemFactory(object):
    def create_problem_output(command: str, args: list[str]) -> str:
        output: str = "Invalid command!"
        if (command in ["expand"]):
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

        return output
        