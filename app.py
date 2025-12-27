from problems.ProblemFactory import ProblemFactory
from mathproblems.MathProblemFactory import MathProblemFactory
from mathproblems.RootExpansion import RootExpansion
from mathproblems.DerivativePolynomial import DerivativePolynomial

from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

def parse_command(input: str):
    input = input.strip()
    words = input.split(" ")
    if (len(words) > 1):
        args = words[1:]
        prob = ProblemFactory.createProblem(words[0], args)
    else:
        prob = ProblemFactory.createProblem(input)
    raw_str = prob.problem_str.rstrip()
    lines = raw_str.split("\n")
    return lines

# Returns a block of MathML
def parse_math_command(input: str) -> str:
    input = input.strip()

    words: list[str] = input.split(" ")
    command: str = words[0] 
    args = words[1:] if len(words) > 1 else []
    return MathProblemFactory.create_problem_output(command, args) 

# Markdown language containing the table of commands and description.
def help_section():
    raw_str = f"""
| Commands | Description |  
|:--|:--|  
|`bst`, `bstdraw`, `bstproblem` | Draw a **Binary Search Tree**. |  
|`heap` | Compute operations on a min-heap and draw out the result. |  
|`sort n`, `sorting n` | Generate n number of arithmetic problems. 0 <= n <= 20 |  
|`conv [b | d | h]` | Generate five random numbers between 0-255 in either binary, decimal, or hexadecimal and write them down in other number systems. | 
"""
    
    html_inst = markdown.markdown(raw_str, extensions=['tables'])
    return html_inst

def math_help_section() -> str:
    raw_str: str = f"""
| Commands | Description |
|:--|:--|
|`arith n` | Generate n numbers of basic arithmetic problems. 1 <= n <= 8 | 
|`expand n` | Expand n binomials algebraically. 2 <= n <= 5 | 
|`derive n` | Generate a polynomial of degree n and take the derivative of it. 1 <= n <= 5 |
|`int n` | Generate a polynomial of degree n and evaluate the integral of it. 1 <= n <= 5 |
|`matsys n` | Generate an augmented matrix that represents a linear system of n variables. 2 <= n <= 5 |
|`psys` | Generate a 2x2 matrix and find its eigenvalues and eigenvectors. Then interpret the matrix in the context of differential equations. |
|`diffeq` | Generate a second order constant coefficient differential equation. |
"""
    html_inst = markdown.markdown(raw_str, extensions=['tables'])
    return html_inst
# --------------------------------------------------------------------------------

@app.route("/math_problem_generator", methods=["GET", "POST"])
def math_problem_generator():
    math_help_table: str = math_help_section()
    mathml_block: str = "<div>Enter a command above!</div>" 

    if (request.method == "POST"):
        user_input: str = request.form["command_line"]
        mathml_block = parse_math_command(user_input)

    return render_template("math_problem_generator.html", math_problem=mathml_block, math_help_section_markdown=math_help_table)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/", methods=["GET", "POST"])
def index():
    # loading some things
    help_section_html = help_section()
    if (request.method == "POST"):
        user_input = request.form["command_line"]
        output_lines = parse_command(user_input)
        return render_template("index.html", output_lines=output_lines, help_section_markdown=help_section_html)
    
    return render_template("index.html", output_lines=["Enter a command above!"], help_section_markdown=help_section_html)

def main():
    app.run()

if (__name__ == "__main__"):
    main()