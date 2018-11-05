from binary_string_generator import *
from algorithms import *

def prettyPrintMatches(text, pat, matches, same_results):
    print("-"*50)
    if same_results:
        print("All algorithms have same results")
    else:
        print("One or more algorithms have different results")
    print("Pattern  : {}".format(pat))
    print("String   : {}".format(text))
    string = ""
    for i in range(len(text)):
        if i in matches:
            string += "^"
        else:
            string += " "
    print("Matches  : {}".format(string))
    print("-"*50)

test_text1 = "ABRACADABRA"
test_pat1 = "BRA"

test1_naive = naive(test_text1, test_pat1)
test1_kmp = KMP(test_text1, test_pat1)
test1_bm = BM(test_text1, test_pat1)
prettyPrintMatches(test_text1, test_pat1, test1_naive, test1_naive==test1_kmp==test1_bm)

test_text2 = "AABAACAADAABAAABAA"
test_pat2 = "AABA"
test2_naive = naive(test_text2, test_pat2)
test2_kmp = KMP(test_text2, test_pat2)
test2_bm = BM(test_text2, test_pat2)
prettyPrintMatches(test_text2, test_pat2, test2_naive, test2_naive==test2_kmp==test2_bm)

test_text3 = generateString(length=30, p=0.5)
test_pat3 = generateString(length=5, p=0.5)
test3_naive = naive(test_text3, test_pat3)
test3_kmp = KMP(test_text3, test_pat3)
test3_bm = BM(test_text3, test_pat3)
prettyPrintMatches(test_text3, test_pat3, test3_naive, test3_naive==test3_kmp==test3_bm)

