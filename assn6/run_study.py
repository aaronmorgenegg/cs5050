import timeit

from binary_string_generator import *
from algorithms import *
from constants import *

ALGORITHMS = ["naive", "kmp", "bm"]

def TimeFunction(function, *args):
    """
    Function to time the runtime of another function
    Call with TimeFunction(function_name, arg1, arg2, ...,argn)
    """
    start_time = timeit.default_timer()
    function(*args)
    return timeit.default_timer() - start_time

def RunStudy():
    #runBinaryStudy()
    runShakespeareStudy()
    runDNAStudy()

def runBinaryStudy():
    if VERBOSITY > 1: print("Generating random binary string...")
    binary_random = generateString(p=0.5)
    for algorithm in ALGORITHMS:
        iterateM(algorithm, binary_random, "binary_random")
    del binary_random
    if VERBOSITY > 1: print("Generating regular binary string...")
    binary_regular = generateString(p=0.999)
    for algorithm in ALGORITHMS:
        iterateM(algorithm, binary_regular, "binary_regular")

def runShakespeareStudy():
    if VERBOSITY > 1: print("Loading complete works of Shakespeare...")
    shakespeare = loadFileToString(STRING_SHAKESPEARE)
    for algorithm in ALGORITHMS:
        iterateM(algorithm, shakespeare, "shakespeare")

def runDNAStudy():
    if VERBOSITY > 1: print("Loading DNA sequence string...")
    dna = loadFileToString(STRING_DNA1)
    for algorithm in ALGORITHMS:
        iterateM(algorithm, dna, "dna")

def loadFileToString(filename):
    with open(filename, 'r') as myfile:
        return myfile.read()

def lookupAlgorithm(algorithm):
    if algorithm == "naive": return naive
    if algorithm == "kmp": return KMP
    if algorithm == "bm": return BM

def iterateM(algorithm, text, study):
    i = MIN_M
    function = lookupAlgorithm(algorithm)
    while i < MAX_M:
        if VERBOSITY > 1: 
            print("Running {} study with {} algorithm with m={}".format(study, algorithm, i))
        pattern = text[-i:]
        time = TimeFunction(function, text, pattern)
        saveData(algorithm, study, i, time)
        i *= 2

def getFilename(algorithm, study):
    return FILENAME_ROOT.format(study, algorithm)

def saveData(algorithm, study, m, runtime):
    filename = getFilename(algorithm, study)
    with open(filename, "a") as myfile:
        myfile.write(str(m)+","+str(runtime)+"\n")

RunStudy()

