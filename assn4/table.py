#!/usr/bin/env python3

########################
# Aaron Morgenegg, A02072659
# Read in dna_alignements and output
# data in table format
########################

import re
from tabulate import tabulate

SRC_DIR = "dna_alignments/{}"
OUT_DIR = "tables/{}"

def readLine(filename):
    with open(filename, 'r') as myfile:
        data=myfile.readline()
    data = re.sub('[^-1234567890]', '', data)
    return data

def getFilename(A, B):
    output_file = re.sub(".txt", "", A) + '-' + re.sub(".txt", "", B)
    return SRC_DIR.format(output_file+".txt")

def makeList(files):
    data = []
    for i in range(len(files)):
        data.append([None]*len(files))
    # makes list of lists containing difference data
    for i in range(len(files)-1):
        for j in range(i+1, len(files)):
            filename = getFilename(files[i], files[j])
            difference = readLine(filename)
            data[i][j] = difference
            data[j][i] = difference
    return data

def makeTable(data, files, output_file):
    for i in range(len(files)):
        data[i] = [files[i]] + data[i]
    data.insert(0, [None] + files)
    with open(output_file, 'w+') as myfile:
        myfile.write(tabulate(data))

human_study = ["human_american_01.txt",
                "human_australia_01.txt",
                "human_chinese_01.txt",
                "human_egypt_01.txt",
                "human_france_01.txt",
                "human_greece_01.txt",
                "human_israel_01.txt",
                "human_japan_01.txt",
                "human_navajo_01.txt",
                "human_southafrica_01.txt"
                ] 

human_data = makeList(human_study)
makeTable(human_data, human_study, OUT_DIR.format("human_study_table.txt"))

ape_study = ["prototypical_human_01.txt",
                    "baboon_01.txt",
                    "bonobo_01.txt",
                    "chimpanzee_01.txt",
                    "chimpanzee_02.txt",
                    "gorilla_01.txt",
                    "gorilla_02.txt"
                    ]
ape_data = makeList(ape_study)
makeTable(ape_data, ape_study, OUT_DIR.format("ape_study_table.txt"))

