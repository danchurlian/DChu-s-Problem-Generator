from problems.ProblemFactory import ProblemFactory

from flask import Flask, render_template, request
import blinker

app = Flask(__name__)


def parse_command(input: str):
    input = input.strip()
    args = input.split(" ")
    # matrix 3x3 linear system
    # 2x2 diff eq 1st order linear system
    # priority queue
    # binary search drawing
    prob = ProblemFactory.createProblem(input)

    return prob.problem_str


@app.route("/", methods=["GET", "POST"])
def index():
    command_output = ""
    if (request.method == "POST"):
        user_input = request.form["command_line"]
        command_output = parse_command(user_input)
    return render_template("index.html", command_output=command_output)

def main():
    app.run()

if (__name__ == "__main__"):
    main()