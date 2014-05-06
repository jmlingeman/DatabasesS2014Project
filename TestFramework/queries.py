__author__ = 'jennie'

from TestFramework.HashIndex import HashIndex as HI
from TestFramework.BTreeIndex import BTreeIndex as BTI
from TestFramework.RTreeIndex import RTreeIndex as RTI
from TestFramework.Disk import Disk

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
        result.append(idx.get(val))
        
    return result
        
# End of contained

def containedDistinct(vals, idx):
    """ SELECT DISTINCT t.rec
        FROM t
        WHERE t.val IN vals """
        
    temp = []
    result = []
    
    for val in vals:
        distinct(result, [idx.get(val)])
        
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
                                tr = [start:]
                                
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

def occurrencesSeq(vals, trjs, idx)
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

n_blocks = 5
n_blocksize = 10
page_size = 5

n_buckets = 5

db = Disk(n_blocks, n_blocksize, page_size)

hashIndex = HI(disk, n_buckets)
btreeIndex = BTI(disk)

