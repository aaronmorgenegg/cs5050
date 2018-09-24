#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Run 3 studies comparing dna of:
# 1. Prototypical human vs neandertal
# 2. 10 different modern humans
# 3. Prototypical human vs 6 great ape species
# run 'python run_study.py'
########################

from dna import *
from file_reader import *

SRC_DIR = "dna_samples/{}"
OUT_DIR = "dna_alignments/{}"

def runStudy(file_A, file_B, output_file):
    print("Comparing DNA between {} and {}, outputing to {}".format(file_A, file_B, output_file))
    study = DNAMatcher(readFile(file_A), readFile(file_B))
    study.matchDP()
    study.printAlignmentToFile(output_file)

print("Running Study 1: Prototypical human vs neandertal")
runStudy(SRC_DIR.format("prototypical_human_01.txt"),
         SRC_DIR.format("neandertal_01.txt"),
         OUT_DIR.format("prototypical_human_01-neandertal_01.txt"))

