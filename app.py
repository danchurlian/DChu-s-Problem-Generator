from problems.ProblemFactory import ProblemFactory

from flask import Flask, render_template, request
import blinker

app = Flask(__name__)


def parse_command(input: str):
    input = input.strip()
    words = input.split(" ")
    if (len(words) > 1):
        args = words[1:]
        prob = ProblemFactory.createProblem(words[0], args)
    else:
        prob = ProblemFactory.createProblem(input)

    # matrix 3x3 linear system
    # 2x2 diff eq 1st order linear system
    # priority queue
    # binary search drawing
    raw_str = prob.problem_str.rstrip()
    lines = raw_str.split("\n")
    return lines


def get_help_lines() -> str:
    return """
        COMMANDS:\n
        --------:\n
        bstdraw OR bstproblem -> Draw a Binary Search Tree.\n
        matsys [n] -> Solve an nth dimension linear system of equations using Gaussian elimination.\n
    """.split("\n")

# ---------------------------------------------------------------


@app.route("/", methods=["GET", "POST"])
def index():
    help_lines = get_help_lines()
    if (request.method == "POST"):
        user_input = request.form["command_line"]
        output_lines = parse_command(user_input)
        return render_template("index.html", output_lines=output_lines, help_lines=help_lines)
    
    return render_template("index.html", help_lines=help_lines)

def main():
    app.run()

if (__name__ == "__main__"):
    main()