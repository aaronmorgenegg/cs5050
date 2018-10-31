import random

from constants import BINARY_STRING_LENGTH


def generateString(length=BINARY_STRING_LENGTH, p=0.5):
    """Generates a random string of 0's and 1's, with regularity defined by p"""
    string = [random.randint(0, 1)]
    for i in range(1, length):
        if random.uniform(0, 1) < p:
            string.append(string[i-1])
        else:
            if string[i-1] == "0":
                string.append("1")
            else:
                string.append("0")
    return string

