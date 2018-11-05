from binary_string_generator import *
from algorithms import *

def prettyPrintMatches(text, pat, matches):
    print("Pattern  : {}".format(pat))
    print("String   : {}".format(text))
    string = ""
    for i in range(len(text)):
        if i in matches:
            string += "^"
        else:
            string += " "
    print("Matches  : {}".format(string))

test_text1 = "ABRACADABRA"
test_pat1 = "BRA"

test1_naive = naive(test_text1, test_pat1)
prettyPrintMatches(test_text1, test_pat1, test1_naive)

test_text2 = "AABAACAADAABAAABAA"
test_pat2 = "AABA"
test2_naive = naive(test_text2, test_pat2)
prettyPrintMatches(test_text2, test_pat2, test2_naive)

