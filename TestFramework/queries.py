__author__ = 'jennie'

from CreateIndexes import *

def distinct(current, other):
    """ Unifies two sets of query results into a set """
    
    for val in other:
        if val not in current:
            current.append(val)
            
    return current
    
# End of distinct

def count():
    """ SELECT COUNT(*)
        FROM t """
       
    
# End of count

def countDistinct(idx):
    """ SELECT DISTINCT COUNT(*)
        FROM t """
        
# End of countDistinct

def contains(recs, idx):
    """ SELECT t.val
        FROM t
        WHERE t.rec IN recs """
    
    result = []
    
    for rec in recs:
        r = idx.get(rec)
        
        for v in r:
            result.append(v)
            
    return result
        
# End of contains

def containsDistinct(recs, idx):
    """ SELECT DISTINCT t.val
        FROM t
        WHERE t.rec IN recs """
        
    temp = []
    result = []
    
    for rec in recs:
        r = idx.get(rec)
        
        for v in r:
            temp.append(v)
        
        distinct(result, temp)
        
    return result
        
# End of containsDistinct

def contained(vals, idx):
    """ SELECT t.rec
        FROM t
        WHERE t.val IN vals """
        
    result = []
    
    for val in vals:
        res = idx.get(val)
        
        if len(res) != 0:
            result.append(res)
        
    return result
        
# End of contained

def containedDistinct(vals, idx):
    """ SELECT DISTINCT t.rec
        FROM t
        WHERE t.val IN vals """        
    
    result = []
    
    for val in vals:
        res = idx.get(val)
        
        if len(res) != 0:            
            distinct(result, [res])
            
    return result
        
# End of containedDistinct

def nGramSeq(vals, idx):
    """ SELECT t.rec
        FROM t
        WHERE CONCAT(val_1, val_2, ... , val_n) IN t.trj """
        
    result = []
    
    if len(vals) == 1:
        result = contained(vals)
    else:
        trjs = idx.get(vals[0])
        n = len(vals)
        
        if len(trjs[0]) == 1:
            # I have to scan sequentially
            
            start = 0 
            tr = []
            
            for trj in trjs:
                # Scan every trj that the ngram appears in
                start = trj.index(vals[0]) # first occurence of first value in ngram
                tr = trj[start:0] # sub trj from occurance of first ngram value
                
                match = True 
                
                while len(tr) >= n:
                    # no point to go further if the ngram cannot fit
                    
                    for i in range(len(vals)):
                        # scanning the values contained in the ngram
                        
                        if vals[i] != tr[i]:
                            # one of the values doesn't match
                            
                            match = False            
                            
                            if tr.count(vals[0]) > 0:
                                # the trj is not over
                                start = tr[1:].index(vals[0]) + 1
                                tr = trj[start:]
                                
                        break
                        
                    if match == True:
                        # ngram fit fully, no point in scanning the rest of the trj
                        
                        result.append(trj)
                        break
        
        # else:
            #I have location info
            
            # valSets = []            
            # result = []
            # temp = []
            
            # for i in range(len(vals)):
                # valSets.append(idx.get(vals[i]))
            
            # for val in valSets[0][0]:
                
                # flag = True
                
                # for vs in valSets[1:]:
                    
                    # if val[0] not in vs[0]:
                        # flag = False
                        # break
                
                # if flag == True:
                    # temp.append(val)
                
            
            # pass
        
    return result
# End of nGramSeq

def occurrencesSeq(vals, trjs, idx):
    """ SELECT DISTINCT t.val.idx
        FROM t
        WHERE t.val IN (vals) AND
            t.rec IN (trj) """
    
    result = []
    temp = []
    
    for trj in trjs:
        distinct(temp, [idx.get(trj)])
        
    for trj in temp:
        for i in range(len(trj)):
            if trj[i] in vals:
                distinct(result,[i])    
    
    return result

# End of occurrences

#######################################
# Main Program
#######################################

bTree, bTreeLoc2ID, bTreeLoc2IDIdx = create_btree_indexes()

containedVals = contained(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
print("contained:\n\n%s\n" % str(containedVals))

containedValsD = containedDistinct(["MOOR-6-1", "COOL-101-1"], bTreeLoc2ID)
print("containedDistinct:\n\n%s\n" % str(containedVals))