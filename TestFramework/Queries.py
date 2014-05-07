__author__ = 'jennie'

# from Index import Index

def distinct(current, other):
    """ Unifies two sets of query results into a set """

    for val in other:
        if val not in current:
            current.append(val)

    return current

# End of distinct

def count(idx):
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
        res = idx.get(rec)

        if len(res) != 0:
            result.extend(res)

    return result

# End of contains

def containsSeq(recs, idx):
    """ Same as contains but without using a fancy index """
    
    result = []
    
    for trj in idx:
        
        if trj[0] in recs:
            result.extend(trj[1])
            
    return result

# End of containsSeq

def containsDistinct(recs, idx):
    """ SELECT DISTINCT t.val
        FROM t
        WHERE t.rec IN recs """

    result = []

    for rec in recs:
        res = idx.get(rec)

        if len(res) != 0:
            distinct(result, res)

    return result

# End of containsDistinct


def containsDistinctSeq(recs, idx):
    """ Same as containsDistinct but without using a fancy index """
    
    result = []
    
    for trj in idx:
        
        if trj[0] in recs:
            distinct(result, trj[1])
            
    return result
    
# End of containsDistinctSeq

def contained(vals, idx):
    """ SELECT t.rec
        FROM t
        WHERE t.val IN vals """

    result = []

    for val in vals:
        res = idx.get(val)

        if len(res) != 0:
            result.extend(res)

    return result

# End of contained

def containedSeq(vals, idx):
    """ Same as contained but without using a fancy index """
    
    result = []
    
    for val in vals:
    
        for trj in idx:
        
            if val in trj[1]:
                result.append(trj[0])
                
    return result    

# End of containedSeq

def containedDistinct(vals, idx):
    """ SELECT DISTINCT t.rec
        FROM t
        WHERE t.val IN vals """

    result = []

    for val in vals:
        res = idx.get(val)

        if len(res) != 0:
            distinct(result, res)

    return result

# End of containedDistinct

def containedDistinctSeq(vals, idx):
    """ Same as containedDistinct but without using a fancy index """
    
    result = []
    
    for val in vals:
    
        for trj in idx:
        
            if val in trj[1]:
                distinct(result, [trj[0]])
                
    return result    

# End of containedDistinctSeq

def nGram(vals, tidx, lidx):
    """ SELECT t.rec
        FROM t
        WHERE CONCAT(val_1, val_2, ... , val_n) IN t.trj """

    result = []

    if len(vals) == 1:
        result = contained(vals, lidx)

    else:
        trjIs = lidx.get(vals[0])

        # print("trjIs: %s\n" % (str(trjIs))) 

        trjDs = []

        for trj in trjIs:
            trjDs.append(tidx.get(trj))

        # print("trjs: %s\n" % (str(trjs)))

        n = len(vals)

        # if len(trjs[0]) == 1:
        # I have to scan sequentially

        start = 0
        tr = []

        trjs = list(zip(trjIs, trjDs))

        # counter = -1
        for trj in trjs:
            # Scan every trj that the ngram appears in

            # counter += 1

            # print("trj # %i: %s\n" % (counter, str(trj[1])))

            start = trj[1].index(vals[0])  # first occurence of first value in ngram
            tr = trj[1][start:]  # sub trj from occurance of first ngram value

            match = True

            while len(tr) >= n:

                # print ("  start: %i, tr: %s\n" % (start, str(tr)))

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

                    result.append(trj[0])
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

def occurrences(vals, trjs, idx):
    """ SELECT DISTINCT t.val.idx
        FROM t
        WHERE t.val IN (vals) AND
            t.rec IN (trj) """

    result = []
    temp = []
    
    if len(trjs) == 0:
        trjs = [i in range (len(idx))]

    for trj in trjs:
        distinct(temp, [idx.get(trj)])

    for trj in temp:
        for i in range(len(trj)):
            if trj[i] in vals:
                result.append(i)

    return result

# End of occurrences

def occurrencesDistinct(vals, trjs, idx):
    """ SELECT DISTINCT t.val.idx
        FROM t
        WHERE t.val IN (vals) AND
            t.rec IN (trj) """

    result = []
    temp = []
    
    if len(trjs) == 0:
        trjs = [i in range (len(idx))]

    for trj in trjs:
        distinct(temp, [idx.get(trj)])

    for trj in temp:
        for i in range(len(trj)):
            if trj[i] in vals:
                distinct(result, [i])

    return result

# End of occurrencesDistinct

def occurrencesGrouped(vals, trjs, idx):
    """ SELECT DISTINCT t.val.idx
        FROM t
        WHERE t.val IN (vals) AND
            t.rec IN (trj) 
        GROUP BY t.val """
        
    result = []
    
    temp = []
    
    if len(trjs) == 0:
        trjs = [i in range (len(idx))]
    
    for val in vals:
        temp.append([val, idx.get(val)])
        
    print("complex index: %s" % (str(temp[0])))
        
    # if type(temp[0][1]) is tuple:
        
        # occurs = []
        
        # for rec in temp:
            
        
    # else:
        
    return result
        
# End of occurrencesGrouped