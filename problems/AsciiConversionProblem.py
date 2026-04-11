from .Problem import Problem
from .NumberConversionHandler import NumberConversionHandler
import requests
import random

REQUEST_URL: str = "https://random-word-api.herokuapp.com/word"


# Generate a truly random word. This random word contains a random
# amount of letters, and each letter is completely random.
def get_truly_random_word() -> str:
    random_word_length: int = random.randint(5, 10)
    result: str = ""

    for i in range(random_word_length):
        result += chr(random.randint(97, 112))

    return result

# Call the random word API and return the response
def get_random_word() -> str:
    word: str = ""
    response = requests.get(REQUEST_URL, timeout=10)
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
    def __init__(self, prob_type: str, word_type: str = "random"):
        self.prob_type = prob_type
        self.word_type = word_type
        super().__init__()
        

    def _get_problem_str(self):
        word: str = "sample word"
        binary_word: str = ""
        result: str = ""
        english_generated_success: bool = False

        if (self.word_type == "english"):
            # Try getting an English word through an API call
            try:
                word = get_random_word()
                binary_word = get_binary_str(word)
                english_generated_success = True

            except Exception as e:
                print(f"Error getting a word. Reason: {e}")

        if (not english_generated_success or self.word_type == "random"):
            word = get_truly_random_word()
            binary_word = get_binary_str(word)
        
        # Display the problem depending on the type of problem
        if (self.prob_type == "decode"):
            result = f"""Here's a sequence of binary characters. 
{binary_word}
Decode this binary using the ASCII standard."""
            
        else:
            result = f"""Translate this word "{word}" into binary using the ASCII standard."""
            
        return result