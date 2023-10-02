from vendor.AND.AND import AND
from utils.shuffle import shuffle
import string

class Filer:
    def __init__(self, seed=-1):
        """
        Initialize Filer

        Args:
            seed (float): A random seed in the range (0, 1); if negative, it's seeded randomly (default is -1).
        """

        self.rng = AND(p=seed)
        self.random_encryption_key = self.rng.random()
        self.chunks_to_num = []

    def encrypt(self, text: str) -> list:
        """
        Encrypt chunks of text using the Filer encryption formula.

        Args:
            text (str): The string to be encrypted.
        """

        ascii_map = self.__create_ascii_mapping__()
        text_to_chunks = self.__split_text_into_chunks__(text, 4)
        self.chunks_to_num = self.__chucks_to_numbers__(text_to_chunks, ascii_map)

        return [i * self.random_encryption_key**16 for i in self.chunks_to_num]

    def decrypt(self, encrypted_chunks: list) -> list:
        """
        Decrypt chunks of text using the Filer encryption formula.

        Args:
            encrypted_chunks (list): The list of encrypted chunks to be decrypted.
        """

        return [int(i / self.random_encryption_key**16) for i in encrypted_chunks]

    def __create_ascii_mapping__(self) -> dict:
        """
        Create a dictionary mapping characters to their corresponding ASCII values + 10 to avoid cases like 00, 01 or 02.
        """

        ascii_chars = {char: str(i+10) for i, char in enumerate(string.ascii_letters + string.digits + string.punctuation + " ")}
        return ascii_chars

    def __split_text_into_chunks__(self, text: str, max_len: int) -> list:
        """
        Split text into chunks of the specified maximum length.

        Args:
            text (str): The string to be splitted into chunks.
            max_len (int): The maximum length of a string in each chunk.
        """

        chunks = [text[i:i + max_len] for i in range(0, len(text), max_len)]
        return chunks

    def __chucks_to_numbers__(self, chunks: list, ascii_map: dict) -> list:
        """
        Convert chunks of texts to their string of corresponding ASCII values.

        Args:
            chunks (list): List is chunks to be converted into numbers.
        """

        return [self.__text_to_numbers__(chunk, ascii_map) for chunk in chunks]

    def __text_to_numbers__(self, text: str, ascii_map: dict) -> int:
        """
        Convert a chunk of text to a string of corresponding ASCII values.

        Args:
            text (str): The string to be converted into a number.
            aschii_map (dict): The map of all ASCII characters with their corresponding values.
        """

        txt_to_num = ""
        for char in text:
            if char in ascii_map:
                txt_to_num += ascii_map[char]

        return int(txt_to_num)


txt = "Steven Paul Jobs (born Abdul Lateef Jandali, February 24, 1955 - October 5, 2011) was an American business magnate, inventor, and investor. He was the co-founder, chairman, and CEO of Apple; the chairman and majority shareholder of Pixar; a member of The Walt Disney Company's board of directors following its acquisition of Pixar; and the founder, chairman, and CEO of NeXT. He was a pioneer of the personal computer revolution of the 1970s and 1980s, along with his early business partner and fellow Apple co-founder Steve Wozniak."

f = Filer(0.578239823)
e = f.encrypt(txt)
d = f.decrypt(e)
print(f.chunks_to_num)
print()
print(e)
print()
print(d)
