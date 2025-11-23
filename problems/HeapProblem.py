from .Problem import Problem

class HeapProblem(Problem):
    def __init__(self):
        super().__init__()
    
    def _get_problem_str(self):
        num_str = "1 2 3 4 5 6 \n"
        return num_str + "please insert 1."