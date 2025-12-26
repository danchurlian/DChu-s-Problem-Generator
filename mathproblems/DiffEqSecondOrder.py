import random

def _forcing_mathml():
    real_component: int = int(random.random() * 11 - 5)
    imaginary_component: int = int(random.random() * 5)
    if (real_component == 0 and imaginary_component == 0):
        return _forcing_mathml()

    coef: int = 1
    coef_mathml: str = ""

    exponential_mathml: str = ""
    if (real_component != 0):
        exponent_term_mathml: str = "<mi>t</mi>"
        if (abs(real_component) != 1):
            exponent_term_mathml = f"<mn>{real_component}</mn><mo>&InvisibleTimes;</mo>{exponent_term_mathml}"

        exponential_mathml = f"<msup><mi>e</mi><mrow>{exponent_term_mathml}</mrow></msup>"

    imaginary_mathml: str = ""
    if (imaginary_component != 0):
        imaginary_mathml = f"<mo>&InvisibleTimes;</mo>"

        # handling the coefficient edge case
        imaginary_term_mathml: str = "<mi>t</mi>"
        if (imaginary_component != 1):
            imaginary_term_mathml = f"<mn>{imaginary_component}</mn><mo>&InvisibleTimes;</mo>{imaginary_term_mathml}"

        inside_mathml: str = f"<mo>(</mo>{imaginary_term_mathml}<mo>)</mo>"

        choice: int = int(random.random() * 2) 
        if (choice == 0):
            imaginary_mathml += f"<mi>cos</mi><mrow>{inside_mathml}</mrow>"
            pass #cos
        else:
            imaginary_mathml += f"<mi>sin</mi><mrow>{inside_mathml}</mrow>"
            pass #sin

    return f"<mrow>{coef_mathml}{exponential_mathml}{imaginary_mathml}</mrow"

def _y_mathml(order: int):
    y_mathml: str = ""
    if (order == 2):
        y_mathml = "<mi>y</mi><mo>&#x2033;</mo>"
    elif (order == 1):
        y_mathml = "<mi>y</mi><mo>&#x2032;</mo>"
    else:
        y_mathml = "<mi>y</mi>"
    return y_mathml

def _term_mathml(coef: int, order: int):
    result: str = ""
    if (coef != 0):
        if (coef < 0):
            result = "<mo>-</mo>"
        elif (coef > 0):
            result = "<mo>+</mo>" 
        
        if (abs(coef) != 1):
            result += f"<mrow><mn>{abs(coef)}</mn><mo>&InvisibleTimes;</mo>"
        result += f"{_y_mathml(order)}</mrow>" 
    return result

# TODO: extract coefficients from the characteristic equation and construct the mathml that way
def _new_diffeq():
    # 2 random roots
    r1: int = int(random.random() * 11 - 5)
    r2: int = int(random.random() * 11 - 5)
    if (r1 == 0 and r2 == 0):
        return _new_diffeq()

    forcing: str = _forcing_mathml() 
    # r,t = sp.symbols("r t")
    # y = sp.Function("y")
    # if (r1 == 0 or r2 == 0):
    #     return _random_quadratic()
    # diff_eq = sp.Eq(y(t).diff(t,t) + (-r1-r2) * y(t).diff(t,1) + (r1*r2) * y(t), 0)
    # char_eq = r ** 2 + (-r1-r2) * r + (r1*r2)
    # print(diff_eq)
    # diff_eq_mathml = sp.mathml(diff_eq, printer="presentation")
    # sp.print_mathml(diff_eq, printer="presentation")

    # args = char_eq.args
    # print(args)
    # return f"<math>{diff_eq_mathml}</math>"
    
    return f"""
<math>
    <mrow>
        <mi>y</mi>
        <mo>&#x2033;</mo>   
        {_term_mathml(-r1 - r2, 1)}
        {_term_mathml(r1 * r2, 0)}
        <mo>=</mo>
        <mrow>{forcing}</mrow>
    </mrow>
</math>
"""

class DiffEqSecondOrder(object):
    def __init__(self): 
        pass

    def get_mathml(self):
        return f"""
<div>Provide the general solution to the second order constant coefficient  linear differential equation below:</div>
<div>
    {_new_diffeq()}
</div>
"""