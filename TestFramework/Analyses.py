__author__ = 'jesse,jennie'

# Class for generating all of our graphs

from DataParser import read_trajectory_data
from Queries import *
from CreateIndexes import *
from numpy import zeros

#######################################
# Main Program
#######################################

data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")
bTree, bTreeLoc2ID, bTreeLoc2IDIdx = create_btree_indexes()
hash, hashLoc2ID, hashLoc2IDIdx = create_hash_indexes()

flatSize = len(data)

flatReads = zeros(flatSize, numpy.int)
flatWrites = ones(flatSize, numpy.int)

######################################
# No Index Section
######################################

containsValsS = containsSeq([30, 47], data, flatReads)
# print("containsSeq: count: %i\n\n%s\n" % (len(containsValsS), str(containsValsS)))

containsValsDS = containsDistinctSeq([30, 47], data, flatReads) 
# print("containsDistinctSeq: count: %i\n\n%s\n" % (len(containsValsDS), str(containsValsDS)))

containedValsS = containedSeq(["MOOR-6-1", "COOL-101-1"], data, flatReads)
# print("containedSeq: count: %i\n\n%s\n" % (len(containedValsS), str(containedValsS)))

containedValsDS = containedDistinctSeq(["MOOR-6-1", "COOL-101-1"], data, flatReads)
# print("containedDistinctSeq: count: %i\n\n%s\n" % (len(containedValsDS), str(containedValsDS)))

#######################################
# Hash Index Section
#######################################

#####################################
# Trj ID index
#####################################

containsValsH = contains([30, 47], hash)
# print("containsH: count: %i\n\n%s\n" % (len(containsValsH), str(containsValsH)))
print("containsH: count: %i; \nStats: %s\n" % (len(containsValsH), str(hash.get_statistics())))

containsValsDH = containsDistinct([30, 47], hash) 
# print("containsDistinctH: count: %i\n\n%s\n" % (len(containsValsDH), str(containsValsDH)))
print("containsDistinctH: count: %i; \nStats: %s\n" % (len(containsValsDH), str(hash.get_statistics())))

occurrencesH = occurrences(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], hash)
# print("occurrencesH: count: %i\n\n%s\n" % (len(occurrencesH), str(occurrencesH)))
print("occurrencesH: count: %i; \nStats: %s\n" % (len(occurrencesH), str(hash.get_statistics())))

occurrencesDistinctH = occurrencesDistinct(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], hash)
# print("occurrencesDistinctH: count: %i\n\n%s\n" % (len(occurrencesDistinctH), str(occurrencesDistinctH)))
print("occurrencesDistinctH: count: %i; \nStats: %s\n" % (len(occurrencesDistinctH), str(hash.get_statistics())))

#####################################
# Loc ID index
#####################################

containedValsH = contained(["MOOR-6-1", "COOL-101-1"], hashLoc2ID)
# print("containedH: count: %i\n\n%s\n" % (len(containedValsH), str(containedValsH)))
print("containedValsH: count: %i; \nStats: %s\n" % (len(containedValsH), str(hashLoc2ID.get_statistics())))

containedValsDH = containedDistinct(["MOOR-6-1", "COOL-101-1"], hashLoc2ID)
# print("containedDistinctH: count: %i\n\n%s\n" % (len(containedValsDH), str(containedValsDH)))
print("containedValsDH: count: %i; \nStats: %s\n" % (len(containedValsDH), str(hashLoc2ID.get_statistics())))

ngramH = nGram(["CHAD-405-1", "CHAD-405-1"], hash, hashLoc2ID)
# print("nGramH: count: %i\n\n%s\n" % (len(ngramH), str(ngramH)))
print("ngramH: count: %i; \nStats: %s\n" % (len(ngramH), str(hashLoc2ID.get_statistics())))

#######################################
# BTree Index Section
#######################################

####################################
# Trj ID Index
####################################

containsValsB = contains([30, 47], bTree)
# print("containsB: count: %i\n\n%s\n" % (len(containsValsB), str(containsValsB)))
print("containsB: count: %i; \nStats: %s\n" % (len(containsValsB), str(bTree.get_statistics())))

containsDistinctB = containsDistinct([30, 47], bTree) 
# print("containsDistinctB: count: %i\n\n%s\n" % (len(containsValsDB), str(containsValsDB)))
print("containsDistinctB: count: %i; \nStats: %s\n" % (len(containsDistinctB), str(bTree.get_statistics())))

occurrencesB = occurrences(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], bTree)
# print("occurrencesB: count: %i\n\n%s\n" % (len(occurrencesB), str(occurrencesB)))
print("ngramB: count: %i; \nStats: %s\n" % (len(occurrencesB), str(bTree.get_statistics())))

occurrencesDistinctB = occurrencesDistinct(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], bTree)
# print("occurrencesDistinctH: count: %i\n\n%s\n" % (len(occurrencesDistinctB), str(occurrencesDistinctB)))
print("ngramB: count: %i; \nStats: %s\n" % (len(occurrencesDistinctB), str(bTree.get_statistics())))

####################################
# Loc ID Index
####################################

containedValsB = contained(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# print("containedB: count: %i\n\n%s\n" % (len(containedValsB), str(containedValsB)))
print("containedValsB: count: %i; \nStats: %s\n" % (len(containedValsB), str(bTreeLoc2ID.get_statistics())))

containedValsDB = containedDistinct(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# print("containedDistinctB: count: %i\n\n%s\n" % (len(containedValsDB), str(containedValsDB)))
print("containedValsDB: count: %i; \nStats: %s\n" % (len(containedValsDB), str(bTreeLoc2ID.get_statistics())))

ngramB = nGram(["CHAD-405-1", "CHAD-405-1"], bTree, bTreeLoc2ID)
# print("nGramB: count: %i\n\n%s\n" % (len(ngramB), str(ngramB)))
print("ngramB: count: %i; \nStats: %s\n" % (len(ngramB), str(bTreeLoc2ID.get_statistics())))

# occurrencesGrouped(["CHAD-405-1"], [], hashLoc2IDIdx)
