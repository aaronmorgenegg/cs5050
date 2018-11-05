
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

def KMP():
    pass

def BM():
    pass

