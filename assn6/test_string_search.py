from binary_string_generator import *
from algorithms import *

test_text1 = "ABRACADABRA"
test_pat1 = "BRA"

test1_naive = naive(test_text1, test_pat1)
print(test1_naive)

test_text2 = "AABAACAADAABAAABAA"
test_pat2 = "AABA"
test2_naive = naive(test_text2, test_pat2)
print(test2_naive)

