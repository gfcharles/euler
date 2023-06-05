"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code
for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
bytes. The user would keep the encrypted message and the encryption key in different locations, and without both
"halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the
password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right
click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text
must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""
import itertools
import logging
import re
import string

from euler import euler_problem


# @euler_problem(logging_level=logging.DEBUG, timing=True)
@euler_problem()
def euler059(filename: str) -> int:
    cipher_text = read_file(filename)

    # For each possible key, decrypt the cipher text and see if we have an English plain text message.
    for key in itertools.product(string.ascii_lowercase, repeat=3):
        plain_text = decrypt(cipher_text, list(key))
        if is_english_text(plain_text):
            logging.debug(f'Key = {key}')
            logging.debug(plain_text)
            return sum(map(ord, plain_text))


def read_file(filename: str) -> list[int]:
    """
     Reads the encrypted message from the file, which is a comma-separated list of encrypted ASCII values.
    """
    with open(f'./euler_data/{filename}') as data_file:
        return list(map(int, data_file.read().split(',')))


def decrypt(values: list[int], key: list[chr]) -> str:
    """
    Decrypts the array of ASCII values representing the cipher text.
    Returns the plain text as a string
    """
    key_length = len(key)
    key_values = list(map(ord, key))

    return ''.join(chr(value ^ key_values[i % key_length]) for i, value in enumerate(values))


def is_english_text(text):
    """
    Basic test to see if the text is probably English. False positive and negatives are possible.
    """
    return re.search(' the ', text) or re.search(' and ', text)


if __name__ == '__main__':
    print(euler059('0059_cipher.txt'))
