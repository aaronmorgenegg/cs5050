#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Run 3 studies comparing dna of:
# 1. Prototypical human vs neandertal
# 2. 10 different modern humans
# 3. Prototypical human vs 6 great ape species
# run 'python run_study.py'
########################

import re
from dna import *
from file_reader import *

SRC_DIR = "dna_samples/{}"
OUT_DIR = "dna_alignments/{}"

def runStudy(file_A, file_B, output_file):
    print("Comparing DNA between {} and {}, outputing to {}".format(file_A, file_B, output_file))
    study = DNAMatcher(readFile(file_A), readFile(file_B))
    difference = study.matchDP()
    study.traceback()
    study.printAlignmentToFile(output_file)
    return difference

def runPairwiseStudies(files, output_file):
    data = []
    for i in range(len(files)):
        data.append([None]*len(files))
    for i in range(len(files)-1):
        for j in range(i+1, len(files)):
            difference = runStudy(SRC_DIR.format(files[i]),
                                  SRC_DIR.format(files[j]),
                                  getOutputFilename(files[i],files[j])
                                  )
            data[i][j] = difference
            data[j][i] = difference
    return data

def getOutputFilename(A, B):
        output_file = re.sub(".txt", "", A) + '-' + re.sub(".txt", "", B)
        return OUT_DIR.format(output_file + ".txt")

print("Running Study 1: Prototypical human vs neandertal")
runStudy(SRC_DIR.format("prototypical_human_01.txt"), 
         SRC_DIR.format("neandertal_01.txt"),
         getOutputFilename("prototypical_human_01.txt", "neandertal_01.txt")
         )

print("Running Study 2: Pairwise comparison of 10 human sequences")
runPairwiseStudies(["human_american_01.txt",
                    "human_australia_01.txt",
                    "human_chinese_01.txt",
                    "human_egypt_01.txt",
                    "human_france_01.txt",
                    "human_greece_01.txt",
                    "human_israel_01.txt",
                    "human_japan_01.txt",
                    "human_navajo_01.txt",
                    "human_southafrica_01.txt"
                    ],
                    "humans_pairwise")

print("Running Study 3: Prototypical human vs great apes")
runPairwiseStudies(["prototypical_human_01.txt",
                    "baboon_01.txt",
                    "bonobo_01.txt",
                    "chimpanzee_01.txt",
                    "chimpanzee_02.txt",
                    "gorilla_01.txt",
                    "gorilla_02.txt"
                    ],
                    "great_ape_pairwise")

