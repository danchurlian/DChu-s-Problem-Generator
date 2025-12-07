from problems.ProblemFactory import ProblemFactory

from flask import Flask, render_template, request
import blinker
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

def help_section():
    raw_str = f"""- `bst`, `bstdraw`, `bstproblem` | Draw a **Binary Search Tree**.
- `matsys [n]` | Solve an nth dimension linear system of equations. 3 <= n <= 5
- `heap` | Compute operations on a min-heap and draw out the result. 
- `arith [n]`, `arithmetic [n]` | Generate n number of arithmetic problems. 0 <= n <= 20
- `sort [n]`, `sorting [n]` | Generate n number of arithmetic problems. 0 <= n <= 20"""
    html_inst = markdown.markdown(raw_str)
    print(html_inst)
    return html_inst

# ---------------------------------------------------------------

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