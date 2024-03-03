def base10_to_base64(number: float) -> str:
    """
    Convert a number from base 10 to base 64.

    Args:
        number (float): The number that is to be converted.
    """

    base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    converted_numbers = []
    numbers = [int(i) for i in str(number).split(".")]
    for n in numbers:
        k = n
        if k == 0:
            return base64_characters[0]

        base64_result = ""
        while k > 0:
            remainder = k % 64
            base64_result = base64_characters[remainder] + base64_result
            k //= 64

        converted_numbers.append(base64_result)

    return ".".join(converted_numbers)

def base64_to_base10(base64_string: str) -> float:
    """
    Converts a base 64 string to a base 10 decimal number.

    Parameters:
        base64_string (str): The base 64 string to be converted.
    """

    base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    converted_numbers = []
    strings = base64_string.split(".")
    for i in strings:
        decimal_number = 0

        for char in i:
            decimal_number = decimal_number * 64 + base64_characters.index(char)

        converted_numbers.append(str(decimal_number))

    return float(".".join(converted_numbers))
