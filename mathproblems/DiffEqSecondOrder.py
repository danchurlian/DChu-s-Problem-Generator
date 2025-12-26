import random

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
        result += f"<mrow><mn>{abs(coef)}</mn><mo>&InvisibleTimes;</mo>{_y_mathml(order)}</mrow>" 


    return result

# TODO: extract coefficients from the characteristic equation and construct the mathml that way
def _random_quadratic():
    # 2 random roots
    r1: int = int(random.random() * 11 - 5)
    r2: int = int(random.random() * 11 - 5)
    
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
        <mn>0</mn>
    </mrow>
</math>
"""

class DiffEqSecondOrder(object):
    def __init__(self): 
        pass

    def get_mathml(self):
        return f"""
<div>Provide the general solution to the second order constant coefficient homoegeous linear differential equation below:</div>
{_random_quadratic()}
"""