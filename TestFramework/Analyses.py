__author__ = 'jesse,jennie'

# Class for generating all of our graphs

from DataParser import read_trajectory_data
from Queries import *
from CreateIndexes import *
from numpy import zeros, int, arange
from Utils import calc_stats
import matplotlib.pyplot as plt

#######################################
# Main Program
#######################################

data, names, id_to_num, num_to_id, pid_to_place, place_to_pid = read_trajectory_data("../../postFSM.txt")
bTree, bTreeLoc2ID, bTreeLoc2IDIdx = create_btree_indexes()
hash, hashLoc2ID, hashLoc2IDIdx = create_hash_indexes()

flatSize = len(data)
flatWrites = zeros(flatSize, int)

containedStats = {}
containsStats = {}
ngramsStats = {}
occurrensesStats = {}

stats = {}

######################################
# No Index Section
######################################

flatReads = zeros(flatSize, int)
containsValsS = containsSeq([30, 47], data, flatReads)
# print("containsSeq: count: %i\n\n%s\n" % (len(containsValsS), str(containsValsS)))
print("containsValsS: count: %i; \nStats: %s\n" % (len(containsValsS), str(calc_stats(flatReads, flatWrites))))

flatReads = zeros(flatSize, int)
containsValsDS = containsDistinctSeq([30, 47], data, flatReads) 
# print("containsDistinctSeq: count: %i\n\n%s\n" % (len(containsValsDS), str(containsValsDS)))

flatReads = zeros(flatSize, int)
containedValsS = containedSeq(["MOOR-6-1", "COOL-101-1"], data, flatReads)
# print("containedSeq: count: %i\n\n%s\n" % (len(containedValsS), str(containedValsS)))

flatReads = zeros(flatSize, int)
containedValsDS = containedDistinctSeq(["MOOR-6-1", "COOL-101-1"], data, flatReads)
# print("containedDistinctSeq: count: %i\n\n%s\n" % (len(containedValsDS), str(containedValsDS)))

#######################################
# Hash Index Section
#######################################

#####################################
# Trj ID index
#####################################

# hash.disk.reset_stats()
# containsValsH = contains([30, 47], hash)
# stats = hash.get_statistics()
# print("containsH: count: %i\n\n%s\n" % (len(containsValsH), str(containsValsH)))
# print("containsH: count: %i; \nStats: %s\n" % (len(containsValsH), str(stats)))

hash.disk.reset_stats()
containsValsDH = containsDistinct([30, 47], hash) 
stats = hash.get_statistics()
containsStats["hash"] = stats
# print("containsDistinctH: count: %i\n\n%s\n" % (len(containsValsDH), str(containsValsDH)))
print("containsDistinctH: count: %i; \nStats: %s\n" % (len(containsValsDH), str(stats)))

# hash.disk.reset_stats()
# occurrencesH = occurrences(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], hash)
# stats = hash.get_statistics()
# print("occurrencesH: count: %i\n\n%s\n" % (len(occurrencesH), str(occurrencesH)))
# print("occurrencesH: count: %i; \nStats: %s\n" % (len(occurrencesH), str(stats)))

hash.disk.reset_stats()
occurrencesDistinctH = occurrencesDistinct(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], hash)
stats = hash.get_statistics()
occurrensesStats["hash"] = stats
# print("occurrencesDistinctH: count: %i\n\n%s\n" % (len(occurrencesDistinctH), str(occurrencesDistinctH)))
print("occurrencesDistinctH: count: %i; \nStats: %s\n" % (len(occurrencesDistinctH), str(stats)))

#####################################
# Loc ID index
#####################################

# hashLoc2ID.disk.reset_stats()
# containedValsH = contained(["MOOR-6-1", "COOL-101-1"], hashLoc2ID)
# stats = hashLoc2ID.get_statistics()
# print("containedH: count: %i\n\n%s\n" % (len(containedValsH), str(containedValsH)))
# print("containedValsH: count: %i; \nStats: %s\n" % (len(containedValsH), str(stats)))

hashLoc2ID.disk.reset_stats()
containedValsDH = containedDistinct(["MOOR-6-1", "COOL-101-1"], hashLoc2ID)
stats = hashLoc2ID.get_statistics()
containedStats["hash"] = stats
# print("containedDistinctH: count: %i\n\n%s\n" % (len(containedValsDH), str(containedValsDH)))
print("containedValsDH: count: %i; \nStats: %s\n" % (len(containedValsDH), str(stats)))

hashLoc2ID.disk.reset_stats()
ngramH = nGram(["CHAD-405-1", "CHAD-405-1"], hash, hashLoc2ID)
stats = hashLoc2ID.get_statistics()
ngramsStats["hash"] = stats
# print("nGramH: count: %i\n\n%s\n" % (len(ngramH), str(ngramH)))
print("ngramH: count: %i; \nStats: %s\n" % (len(ngramH), str(stats)))

#######################################
# BTree Index Section
#######################################

####################################
# Trj ID Index
####################################

# bTree.reset_stats()
# containsValsB = contains([30, 47], bTree)
# stats = bTree.get_statistics()
# ngramsStats["BTree"] = stats
# print("containsB: count: %i\n\n%s\n" % (len(containsValsB), str(containsValsB)))
# print("containsB: count: %i; \nStats: %s\n" % (len(containsValsB), str(stats)))

bTree.reset_stats()
containsDistinctB = containsDistinct([30, 47], bTree) 
stats = bTree.get_statistics()
containsStats["BTree"] = stats
# print("containsDistinctB: count: %i\n\n%s\n" % (len(containsValsDB), str(containsValsDB)))
print("containsDistinctB: count: %i; \nStats: %s\n" % (len(containsDistinctB), str(bTree.get_statistics())))

# bTree.reset_stats()
# occurrencesB = occurrences(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], bTree)
# stats = bTree.get_statistics()
# ngramsStats["BTree"] = stats
# print("occurrencesB: count: %i\n\n%s\n" % (len(occurrencesB), str(occurrencesB)))
# print("occurrencesB: count: %i; \nStats: %s\n" % (len(occurrencesB), str(stats)))

bTree.reset_stats()
occurrencesDistinctB = occurrencesDistinct(["CHAD-405-1", "CHAD-405-1"], [5993, 9554, 10182, 13385], bTree)
stats = bTree.get_statistics()
occurrensesStats["BTree"] = stats
# print("occurrencesDistinctH: count: %i\n\n%s\n" % (len(occurrencesDistinctB), str(occurrencesDistinctB)))
print("occurrencesDistinctB: count: %i; \nStats: %s\n" % (len(occurrencesDistinctB), str(bTree.get_statistics())))

####################################
# Loc ID Index
####################################

# bTreeLoc2ID.reset_stats()
# containedValsB = contained(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
# stats = bTreeLoc2ID.get_statistics()
# ngramsStats["BTree"] = stats
# print("containedB: count: %i\n\n%s\n" % (len(containedValsB), str(containedValsB)))
# print("containedValsB: count: %i; \nStats: %s\n" % (len(containedValsB), str(bTreeLoc2ID.get_statistics())))

bTreeLoc2ID.reset_stats()
containedValsDB = containedDistinct(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
stats = bTreeLoc2ID.get_statistics()
containedStats["BTree"] = stats
# print("containedDistinctB: count: %i\n\n%s\n" % (len(containedValsDB), str(containedValsDB)))
print("containedValsDB: count: %i; \nStats: %s\n" % (len(containedValsDB), str(stats)))

bTreeLoc2ID.reset_stats()
ngramB = nGram(["CHAD-405-1", "CHAD-405-1"], bTree, bTreeLoc2ID)
stats = bTreeLoc2ID.get_statistics()
ngramsStats["BTree"] = stats
# print("nGramB: count: %i\n\n%s\n" % (len(ngramB), str(ngramB)))
print("ngramB: count: %i; \nStats: %s\n" % (len(ngramB), str(stats)))

# occurrencesGrouped(["CHAD-405-1"], [], hashLoc2IDIdx)

bWidth = 0.4
colors = ['b', 'y']

fig = plt.figure(1)
fig.set_facecolor('white') 

labels = list(containsStats.keys())
values = [val["Total Reads"] for val in containsStats.values()]

plt.subplot(221)    
plt.xlabel("Index Type")
plt.ylabel("Number of Reads")
plt.title("All Distinct Locations Contained within listed Trajectories" )
plt.bar(range(len(labels)), values, width=bWidth, color = colors)
plt.xticks(arange(len(labels)) + 0.5 * bWidth, labels)

labels = list(containedStats.keys())
values = [val["Total Reads"] for val in containedStats.values()]

plt.subplot(222)
plt.xlabel("Index Type")
plt.ylabel("Number of Reads")
plt.title("All Trajectories Containing Listed Locations" )
plt.bar(range(len(labels)), values, width=bWidth, color = colors)
plt.xticks(arange(len(labels)) + 0.5 * bWidth, labels)

labels = list(occurrensesStats.keys())
values = [val["Total Reads"] for val in occurrensesStats.values()]

plt.subplot(223)    
plt.xlabel("Index Type")
plt.ylabel("Number of Reads")
plt.title("Occurrences of Locations in Trajectories (Place)" )
plt.bar(range(len(labels)), values, width=bWidth, color = colors)
plt.xticks(arange(len(labels)) + 0.5 * bWidth, labels)

labels = list(ngramsStats.keys())
values = [val["Total Reads"] for val in ngramsStats.values()]

plt.subplot(224)    
plt.xlabel("Index Type")
plt.ylabel("Number of Reads")
plt.title("All Trajectories Containing Listed nGram" )
plt.bar(range(len(labels)), values, width=bWidth, color = colors)
plt.xticks(arange(len(labels)) + 0.5 * bWidth, labels)

plt.show()
