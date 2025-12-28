import random

def _random_binomial_mathml():
    root: int = int(random.random() * 11 - 5)
    
    return f"""
<mrow>
    <mo>(</mo>
    <mi>y</mi>
    <mo>+</mo>
    <mn>{root}</mn>
    <mo>)</mo>
</mrow>
"""
    
class DiffEqAutonomous(object):
    def __init__(self):
        pass

    def get_mathml(self):
        # Create a chain of binomials on the right-hand side of the ODE
        root_chain_mathml = ""
        for i in range(3):
            root_chain_mathml += _random_binomial_mathml()
        # Return the whole mathml string, which includes the left hand side dydt 
        return f"""
<div>Consider the following autonomous differential equation:</div>
<math>
    <mfrac>
        <mrow>
            <mi>d</mi>
            <mi>y</mi>
        </mrow>
        <mrow>
            <mi>d</mi>
            <mi>t</mi>
        </mrow>
    </mfrac>
    <mo>=</mo>
    {root_chain_mathml}
</math>
<div>Find the stationary points of this ODE.</div>
<div>Sketch a phase portrait of this ODE.</div>
<div>Sketch a family of solutions for this ODE.</div>
<div>Observe how each solution behaves depending on the starting <math><mi>y</mi></math> value for <math><mrow><mi>t</mi><mo>=</mo><mn>0</mn></mrow></math>.</div>
"""