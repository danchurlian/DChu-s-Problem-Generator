class Problem(object):
    def __init__(self):
        self.problem_str = "sample"
        self.problem_str = self._get_problem_str()
    
    def _get_problem_str(self):
        return "Problem not found!"