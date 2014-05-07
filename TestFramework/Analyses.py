__author__ = 'jesse,jennie'

# Class for generating all of our graphs

from DataParser import read_trajectory_data
from Queries import *
from CreateIndexes import *


#######################################
# Main Program
#######################################

data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")
bTree, bTreeLoc2ID, bTreeLoc2IDIdx = create_btree_indexes()
hash, hashLoc2ID, hashLoc2IDIdx = create_hash_indexes()

######################################
# No Index Section
######################################

# containsValsS = containsSeq([30, 47], data)
# print("containsSeq: count: %i\n\n%s\n" % (len(containsValsS), str(containsValsS)))

# containsValsDS = containsDistinctSeq([30, 47], data) 
# print("containsDistinctSeq: count: %i\n\n%s\n" % (len(containsValsDS), str(containsValsDS)))

# containedValsS = containedSeq(["MOOR-6-1", "COOL-101-1"], data)
# print("containedSeq: count: %i\n\n%s\n" % (len(containedValsS), str(containedValsS)))

# containedValsDS = containedDistinctSeq(["MOOR-6-1", "COOL-101-1"], data)
# print("containedDistinctSeq: count: %i\n\n%s\n" % (len(containedValsDS), str(containedValsDS)))

#######################################
# Hash Index Section
#######################################

# containsValsH = contains([30, 47], hash)
# print("containsH: count: %i\n\n%s\n" % (len(containsValsH), str(containsValsH)))

# containsValsDH = containsDistinct([30, 47], hash) 
# print("containsDistinctH: count: %i\n\n%s\n" % (len(containsValsDH), str(containsValsDH)))

# containedValsH = contained(["MOOR-6-1", "COOL-101-1"], hashLoc2ID)
# print("containedH: count: %i\n\n%s\n" % (len(containedValsH), str(containedValsH)))

# containedValsDH = containedDistinct(["MOOR-6-1", "COOL-101-1"], hashLoc2ID)
# print("containedDistinctH: count: %i\n\n%s\n" % (len(containedValsDH), str(containedValsDH)))

# ngramH = nGram(["CHAD-405-1", "CHAD-405-1"], hash, hashLoc2ID)
# print("nGramH: count: %i\n\n%s\n" % (len(ngramH), str(ngramH)))

# occurrencesH = occurrences(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], hash)
# print("occurrencesH: count: %i\n\n%s\n" % (len(occurrencesH), str(occurrencesH)))

# occurrencesDistinctH = occurrencesDistinct(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], hash)
# print("occurrencesDistinctH: count: %i\n\n%s\n" % (len(occurrencesDistinctH), str(occurrencesDistinctH)))

#######################################
# BTree Index Section
#######################################

# containsValsB = contains([30, 47], bTree)
# print("containsB: count: %i\n\n%s\n" % (len(containsValsB), str(containsValsB)))

# containsValsDB = containsDistinct([30, 47], bTree) 
# print("containsDistinctB: count: %i\n\n%s\n" % (len(containsValsDB), str(containsValsDB)))

# containedValsB = contained(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# print("containedB: count: %i\n\n%s\n" % (len(containedValsB), str(containedValsB)))

# containedValsDB = containedDistinct(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# print("containedDistinctB: count: %i\n\n%s\n" % (len(containedValsDB), str(containedValsDB)))

# ngramB = nGram(["CHAD-405-1", "CHAD-405-1"], bTree, bTreeLoc2ID)
# print("nGramB: count: %i\n\n%s\n" % (len(ngramB), str(ngramB)))

# occurrencesB = occurrences(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], bTree)
# print("occurrencesB: count: %i\n\n%s\n" % (len(occurrencesB), str(occurrencesB)))

# occurrencesDistinctB = occurrencesDistinct(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], bTree)
# print("occurrencesDistinctH: count: %i\n\n%s\n" % (len(occurrencesDistinctB), str(occurrencesDistinctB)))

occurrencesGrouped(["CHAD-405-1"], [], hashLoc2IDIdx)