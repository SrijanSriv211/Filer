from src.vendor.AND.AND import AND
import string

def shuffle(lst, random_nums):
    # Pair each string with a random number and sort by the random numbers
    paired_lists = list(zip(random_nums, lst))
    paired_lists.sort(key=lambda x: x[0])

    # Extract the shuffled strings
    return [x[1] for x in paired_lists]

class Filer:
    def __init__(self, seed=-1):
        """
        Initialize Filer

        Args:
            seed (float, optional): A random seed in the range (0, 1); if negative, it's seeded randomly (default is -1).
            max_len (int, optional): The maximum length of a string in each chunk (default is 4).
            common_exponent (int, optional): The common exponent used with the random encryption key to encrypt or decrypt text (default is 8).

        Note:
            max_len, common_exponent (recommended: not to change the default values):
                Higher value = Lesser accuracy in decryption,
                Lower value = Higher accuracy in decryption
        """

        self.max_len = 4

        self.rng = AND(p=seed)
        self.random_encryption_key = self.rng.random()

        self.ascii_map = self.__create_ascii_mapping__()

    def encrypt(self, text: str) -> list:
        """
        Encrypt chunks of text using the Filer encryption formula.

        Args:
            text (str): The string to be encrypted.
        """

        text_to_chunks = self.__text_chunks__(text, self.max_len)
        chunks_to_num = self.__encode_chunks__(text_to_chunks)

        return [chunk_num * self.random_encryption_key for chunk_num in chunks_to_num]

    def decrypt(self, encrypted_chunks: list) -> list:
        """
        Decrypt chunks of text using the Filer encryption formula.

        Args:
            encrypted_chunks (list): The list of encrypted chunks to be decrypted.
        """

        decrypted_chunks = [format(encrypted_chunk_num / self.random_encryption_key, ".0f") for encrypted_chunk_num in encrypted_chunks]
        decrypted_chunks_to_str = self.__decode_chunks__(decrypted_chunks)

        return "".join(decrypted_chunks_to_str)

    def __create_ascii_mapping__(self) -> dict:
        """
        Create a dictionary mapping characters to their corresponding ASCII values + 10 to avoid cases like 00, 01 or 02.
        """

        random_nums = [self.rng.random() for _ in range(len(string.printable))]
        ascii_chars = "".join(shuffle(list(string.printable), random_nums))

        ascii_map = {char: str(i+100) for i, char in enumerate(ascii_chars)}
        return ascii_map

    def __text_chunks__(self, text: str, max_len: int) -> list:
        """
        Split text into chunks of the specified maximum length.

        Args:
            text (str): The string to be splitted into chunks.
            max_len (int): The maximum length of a string in each chunk.
        """

        chunks = [text[i:i + max_len] for i in range(0, len(text), max_len)]
        return chunks

    def __encode_chunks__(self, chunks: list) -> list:
        """
        Encode chunks of texts to their string of corresponding ASCII values.

        Args:
            chunks (list): List is chunks to be encoded into numbers.
        """

        return [self.__encode_text__(chunk) for chunk in chunks]

    def __decode_chunks__(self, chunks: list) -> list:
        """
        Decode chunks of numbers to their string of corresponding ASCII characters.

        Args:
            chunks (list): List is chunks to be decoded into numbers.
        """

        return [self.__decode_text__(chunk) for chunk in chunks]

    def __encode_text__(self, text: str) -> int:
        """
        Encode a text string to a string of it's corresponding ASCII values.

        Args:
            text (str): The string to be encoded into a number.
        """

        number = ""
        for char in text:
            if char in self.ascii_map:
                number += self.ascii_map[char]

        return int(number)

    def __decode_text__(self, number: str) -> str:
        """
        Decode a number to a string of it's corresponding ASCII characters.

        Args:
            number (str): The number to be decoded into a string.
        """

        chunks = self.__text_chunks__(number, 3)
        temp_ascii_map = {idx: char for char, idx in self.ascii_map.items()}

        new_str = ""
        for i in chunks:
            new_str += temp_ascii_map[i]

        return new_str

if __name__ == "__main__":
    txt = "Hello world!"

    f = Filer(0.578239823)
    e = f.encrypt(txt)
    d = f.decrypt(e)

    print(e)
    print(d)
