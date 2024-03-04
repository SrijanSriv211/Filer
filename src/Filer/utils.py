class BaseConversion:
    def Base10_to_base64(decimal_number, precision=8):
        """
        Converts a decimal number with fractions to a base 64 string.

        Parameters:
        - decimal_number (float): The decimal number to be converted.
        - precision (int): The number of decimal places to consider (default is 8).

        Returns:
        - str: The base 64 representation of the decimal number.
        """
        base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        # Separate whole and fractional parts
        whole_part = int(decimal_number)
        fractional_part = decimal_number - whole_part

        # Convert whole part to base 64
        whole_base64 = BaseConversion.Base10_integer_to_base64(whole_part)

        # Convert fractional part to base 64
        fractional_base64 = BaseConversion.Base10_fraction_to_base64(fractional_part, precision)

        # Combine whole and fractional parts
        base64_result = whole_base64 + "." + fractional_base64

        return base64_result

    def Base10_integer_to_base64(integer):
        """
        Converts an integer to its base 64 representation.

        Parameters:
        - integer (int): The integer to be converted.

        Returns:
        - str: The base 64 representation of the integer.
        """
        base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        
        if integer == 0:
            return base64_characters[0]

        base64_result = ""
        while integer > 0:
            remainder = integer % 64
            base64_result = base64_characters[remainder] + base64_result
            integer //= 64

        return base64_result

    def Base10_fraction_to_base64(fraction, precision):
        """
        Converts a fractional part to its base 64 representation.

        Parameters:
        - fraction (float): The fractional part to be converted.
        - precision (int): The number of decimal places to consider.

        Returns:
        - str: The base 64 representation of the fractional part.
        """
        base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        
        fraction_base64 = ""
        for _ in range(precision):
            fraction *= 64
            digit = int(fraction)
            fraction_base64 += base64_characters[digit]
            fraction -= digit

        return fraction_base64

    def Base64_to_base10(base64_string):
        """
        Converts a base 64 string to a decimal number.

        Parameters:
        - base64_string (str): The base 64 string to be converted.

        Returns:
        - float: The decimal representation of the base 64 string.
        """
        parts = base64_string.split(".")
        whole_part = BaseConversion.Base64_integer_to_base10(parts[0])
        fractional_part = BaseConversion.Base64_fraction_to_base10(parts[1])

        return whole_part + fractional_part

    def Base64_integer_to_base10(base64_string):
        """
        Converts a base 64 string to an integer.

        Parameters:
        - base64_string (str): The base 64 string to be converted.

        Returns:
        - int: The integer representation of the base 64 string.
        """
        base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        decimal_number = 0

        for char in base64_string:
            decimal_number = decimal_number * 64 + base64_characters.index(char)

        return decimal_number

    def Base64_fraction_to_base10(base64_string):
        """
        Converts a base 64 string to a fractional part.

        Parameters:
        - base64_string (str): The base 64 string to be converted.

        Returns:
        - float: The fractional part representation of the base 64 string.
        """
        base64_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        fractional_part = 0.0
        base64_length = len(base64_string)

        for i in range(base64_length):
            digit = base64_characters.index(base64_string[i])
            fractional_part += digit / (64 ** (i + 1))

        return fractional_part

class BPE:
    pass
