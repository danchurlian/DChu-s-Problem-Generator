from .Problem import Problem
from .NumberConversionHandler import NumberConversionHandler
import requests

REQUEST_URL: str = "https://random-word-api.herokuapp.com/word"

# Call the random word API and return the response
def get_random_word() -> str:
    word: str = ""
    response = requests.get(REQUEST_URL)
    response.raise_for_status()

    # Response content is a list with a single element ["random"]
    word = response.json()[0]
    return word

# Given a random word "random", return a string which is a sequence 
# of ASCII binary representations for each character.
def get_binary_str(word: str) -> str:
    result: str = ""
    for i, letter in enumerate(word):
        if (i == 0):
            letter = letter.capitalize()
        code: int = ord(letter)
        char_binary: str = NumberConversionHandler.decimal_to_binary(code)
        result += f"{char_binary} "
    return result


class AsciiConversionProblem(Problem):
    def __init__(self, prob_type: str):
        self.prob_type = prob_type
        super().__init__()
        

    def _get_problem_str(self):
        word: str = "sample word"
        binary_word: str = ""
        result: str = ""
        try:
            word = get_random_word()
            binary_word = get_binary_str(word)
        except Exception as e:
            return f"Failed to get a random word. Error: {e}"
        
        # Display the problem depending on the type of problem
        if (self.prob_type == "decode"):
            result = f"""Here's a sequence of binary characters. 
{binary_word}
Decode this binary using the ASCII standard."""
            
        else:
            result = f"""Translate this word "{word}" into binary using the ASCII standard."""
            
        return result