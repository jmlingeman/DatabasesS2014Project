__author__ = 'jennie'

from HashIndex import HashIndex as HI

def count():
    """ SELECT COUNT(*)
        FROM t """
       
    
# End of count

def countDistinct():
    """ SELECT DISTINCT COUNT(*)
        FROM t """
        
# End of countDistinct

def contains(recs):
    """ SELECT t.val
        FROM t
        WHERE t.rec IN recs """
        
# End of contains

def containsDistinct(recs):
    """ SELECT DISTINCT t.val
        FROM t
        WHERE t.rec IN recs """
        
# End of containsDistinct

def contained(vals):
    """ SELECT t.rec
        FROM t
        WHERE t.val IN vals """
        
# End of contained

def containedDistinct(vals):
    """ SELECT DISTINCT t.rec
        FROM t
        WHERE t.val IN vals """
        
# End of containedDistinct

def nGram(vals):
    """ SELECT t.rec
        FROM t
        WHERE CONCAT(val_1, val_2, ... , val_n) IN t.trj """
    
    if len(vals) == 1:
        contained(vals)
        #...
        
# End of nGram

def distinct(current, other):
    """ Unifies two sets of query results into a set """
    
    for val in other:
        if val not in current:
            current.append(val)
            
    return current
    
# End of distinct