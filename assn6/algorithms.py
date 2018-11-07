from constants import *


def naive(text, pattern):
    found_indices = []
    n = len(text)
    m = len(pattern)
    for i in range(n-m+1):
        for j in range(m):
            if text[i+j] != pattern[j]:
                break
            if j == m-1:
                found_indices.append(i)
    return found_indices

def KMP(text, pattern):
    """https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/"""
    found_indices = []
    n = len(text)
    m = len(pattern)

    # precompute prefix/suffix array
    lps = [0]*m
    computeLPSArray(pattern, m, lps)

    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            found_indices.append(i-j)
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]:
            if j!= 0:
                j = lps[j-1]
            else:
                i += 1
    
    return found_indices

def computeLPSArray(pattern, m, lps):
    """https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/"""
    length = 0

    i = 1
    while i < m:
        if pattern[i]==pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

def badCharHeuristic(string, size):
    bad_char = [-1]*NUM_CHARS
    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char

def BM(text, pattern):
    """https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/"""
    m = len(pattern)
    n = len(text)
    found_indices = []

    bad_char = badCharHeuristic(pattern, m)

    s = 0
    while (s<= n-m):
        j = m-1

        while j >= 0 and pattern[j] == text[s+j]:
            j -= 1

        if j<0:
            found_indices.append(s)
            s += (m-bad_char[ord(text[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-bad_char[ord(text[s+j])])

    return found_indices

