from problems.ProblemFactory import ProblemFactory
from mathproblems.RootExpansion import RootExpansion

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
    problem = RootExpansion()
    return problem.get_mathml()

def help_section():
    raw_str = f"""
| Commands | Description |  
|:--|:--|  
| `bst`, `bstdraw`, `bstproblem` | Draw a **Binary Search Tree**. |  
|`matsys n` | Solve an nth dimension linear system of equations. 3 <= n <= 5 |
|`heap` | Compute operations on a min-heap and draw out the result. |  
|`arith n`, `arithmetic n` | Generate n number of arithmetic problems. 0 <= n <= 20 |  
|`sort n`, `sorting n` | Generate n number of arithmetic problems. 0 <= n <= 20 |  
|`psys`, `diffsys`, `planarsys` | Generate a 2x2 matrix which has integer eigenvalues and integer eigenvectors. |  
|`conv [b | d | h]` | Generate five random numbers between 0-255 in either binary, decimal, or hexadecimal and write them down in other number systems. | 
"""
    
    html_inst = markdown.markdown(raw_str, extensions=['tables'])
    print(html_inst)
    return html_inst

# ---------------------------------------------------------------

@app.route("/math_problem_generator", methods=["GET", "POST"])
def math_problem_generator():
    if (request.method == "POST"):
        user_input: str = request.form["command_line"]
        mathml_block: str = parse_math_command(user_input)
        return render_template("math_problem_generator.html", math_problem=mathml_block)
        print(f"This is a post request with {user_input}")
    return render_template("math_problem_generator.html")

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