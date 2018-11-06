
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

def BM(text, pattern):
    return naive(text, pattern)

