class NumberConversionHandler(object):
    # This class contains utility functions that convert various forms of integers to those of other bases.

    # num -> a number between 0 and 255, inclusive.
    # result -> an 8-bit binary number represented as a string.
    def decimal_to_binary(num: int) -> str:
        result: str = ""
        for i in range(7, -1, -1):
            digit_value: int = 2 ** i
            if (num >= digit_value):
                result += "1"
                num -= digit_value
            else:
                result += "0"
        return result