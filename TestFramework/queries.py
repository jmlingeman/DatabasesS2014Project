__author__ = 'jennie'

from HashIndex import HashIndex as HI
from BTreeIndex import BTreeIndex as BTI
from RTreeIndex import RTreeIndex as RTI
from Disk import *

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
        if len(trjs) == 1:
            # I have to scan sequentially
        
        else:
            #I have location info
            
            pass
        
    return result
# End of nGramSeq

def occurrences(val, trj, idx)
    """ SELECT t.val.idx
        FROM t
        WHERE t.val IN (vals) AND
            t.rec IN (trj) """

# End of occurrences

def distinct(current, other):
    """ Unifies two sets of query results into a set """
    
    for val in other:
        if val not in current:
            current.append(val)
            
    return current
    
# End of distinct

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

