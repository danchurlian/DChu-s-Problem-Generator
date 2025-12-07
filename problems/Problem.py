class Problem(object):
    def __init__(self, custom_problem_str=None):
        if (custom_problem_str != None):
            self.problem_str = custom_problem_str
        else:
            self.problem_str = self._get_problem_str()
            
    def _get_problem_str(self):
        return "Problem not found!"