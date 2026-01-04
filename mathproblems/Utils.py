import random

def polynomial_new_term(exponent: int, start: bool) -> str:
    result: str = ""
    # coef should not be 0
    coef: int = int(random.random() * 13 - 6)
    while (coef == 0):
        coef = int(random.random() * 13 - 6)

    if (abs(coef) == 1):
        if (coef < 0):
            result += f"<mo>-</mo>"
        elif not start:
            result += f"<mo>+</mo>"
    else:
        if (coef < 0):
            result = f"<mo>-</mo><mn>{-coef}</mn>"
        else:
            if start:
                result += f"<mn>{coef}</mn>" 
            else:
                result += f"<mo>+</mo><mn>{coef}</mn>"

    exponential: str = ""
    if (exponent > 1):
        exponential = f"<msup><mi>x</mi><mn>{exponent}</mn></msup>" 
    elif (exponent == 1):
        exponential = f"<mi>x</mi>"
    elif (abs(coef) == 1):
        exponential = f"<mn>1</mn>"
    result += exponential

    return result

class Utils(object):
    def polynomial(degree: int) -> str:
        expression: str = ""
        for i in range(degree, -1, -1):
            expression += polynomial_new_term(i, False) if i < degree else polynomial_new_term(i, True)
        return expression

    # Note this has only worked for inputs of trig functions  
    def combine_coef_var(coef: int, var: str):
        result: str = ""
        var_id: str = f"<mi>{var}</mi>"
        # coef = 0 -> Nothing, depends adding or multiplying or single thing
        # coef = 1 -> return var
        if (coef == 0):
            pass
        elif (coef == 1):
            result = var_id
        else:
            result = f"""
<mn>{coef}</mn>
<mo>&InvisibleTimes;</mo>
{var_id}
"""
        return result

    def raise_power(mathml_expression: str, power: int, mode: str = "times"):
        result: str = ""
        if (mode == "times"):
            # 0 -> nothing
            # 1 -> expression alone
            if (power != 0):
                if (power == 1):
                    result = mathml_expression
                else:
                    result = f"""
<msup>
    {mathml_expression}
    <mn>{power}</mn>
</msup>
"""
        return result

    # Handles parenthesis for trig functions
    # trig_function may be "sin", "cos", "tan", etc.
    def raise_trig_power(trig_function: str, arg_expr: str, power: int):
        result: str = ""
        if (power != 0):
            result = f"""
{Utils.raise_power(f"<mi>{trig_function}</mi>", power, "times")}
<mo>(</mo>
{arg_expr}
<mo>)</mo>
"""
        return result