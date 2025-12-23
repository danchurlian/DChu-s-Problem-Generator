import random, math
import numpy as np

def _p_random():
    D = 1 # set determinant
    a = int((random.random() * 4 + 1) * math.pow(-1, int(random.random() * 2)))
    c = int(random.random() * 4 + 1)
    d = int(random.random() * 4 + 1)
    numerator = (D + c*d)
    while (a != 1 and a != -1 and numerator % a != 0):
        c = int(random.random() * 4 + 1)
        d = int(random.random() * 4 + 1)
        numerator = (D + c*d)
        print(numerator, numerator % a)
    b = int((numerator) / a)
    
    return a,b,c,d

def _get_matrix():
    success: bool = True

    # Random eigenvalues
    e_value_1: int = int((random.random() * 4 + 1) * math.pow(-1, int(random.random() * 2)))
    e_value_2: int = int((random.random() * 4 + 1) * math.pow(-1, int(random.random() * 2)))

    a,b,c,d = _p_random()
    diag = np.array([[e_value_1, 0], [0, e_value_2]], np.int32)
    p = np.array([[a, c], [d, b]], np.int32)
    
    result = None
    try:
        result = np.astype(p @ diag @ np.linalg.inv(p), np.int32)
    except np.linalg.LinAlgError:
        success = False
    if (not success):
        result = _get_matrix()

    print(f"P matrix is {p}")
    print(f"Diagonal matrix is {diag}")
    print(f"Result is {result}")
    return result

class LinearPlanarSystem(object):
    def __init__(self):
        pass

    def get_mathml(self):
        matrix = _get_matrix()
        matrix_str: str = "<mo>[</mo><mtable>\n" 
        for i in range(len(matrix)):
            matrix_str += "<mtr>\n"
            for j in range(len(matrix[i])):
                matrix_str += f"<mtd>{matrix[i][j]}</mtd>\n" 
            matrix_str += "</mtr>\n"
        matrix_str += "</mtable>\n<mo>]</mo>"
        return f"""
<div>Given this 2x2 matrix:</div>
<div>
    <math>
        <mrow>
            <mi>A</mi>
            <mo>=</mo>
            {matrix_str}
        </mrow>
    </math>
</div>
<div>Find the eigenvalues and eigenvectors.</div>
<div>In the context of differential equations, find the general solution of the linear planar system.</div>
<div>
    Using the eigenvalues and eigenvectors, find the exponential
    <math>
        <mrow>
            <msup>
                <mi>e</mi>
                <mrow>
                    <mi>t</mi>
                    <mi>A</mi>
                </mrow>
            </msup>
        </mrow>
    </math>
    .
</div>
<div>Sketch the phase portrait of the linear planar system.</div>
"""