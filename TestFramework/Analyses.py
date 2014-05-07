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

# containedVals = contained(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# print("contained: count: %i\n\n%s\n" % (len(containedVals), str(containedVals)))

# containedValsD = containedDistinct(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# print("containedDistinct: count: %i\n\n%s\n" % (len(containedValsD), str(containedValsD)))

# containsVals = contains([30, 47], bTree)
# print("contains: count: %i\n\n%s\n" % (len(containsVals), str(containsVals)))

# containsValsD = containsDistinct([30, 47], bTree) 
# print("containsDistinct: count: %i\n\n%s\n" % (len(containsValsD), str(containsValsD)))

# Get the dataset from the dataparser, and its corresponding helpers
# This is a bit wasteful because it is already read in in CreateIndexes, but whatever. The file isn't too large.

# ngram = nGram(["CHAD-405-1", "CHAD-405-1"], bTree, bTreeLoc2ID)
# print("nGramSeq: count: %i\n\n%s\n" % (len(ngram), str(ngram)))

containedValsS = containsSeq(["MOOR-6-1", "COOL-101-1"], data)
print("contained: count: %i\n\n%s\n" % (len(containedValsS), str(containedValsS)))

containedValsDS = containsDistinctSeq(["MOOR-6-1", "COOL-101-1"], data)
print("containedDistinct: count: %i\n\n%s\n" % (len(containedValsDS), str(containedValsDS)))