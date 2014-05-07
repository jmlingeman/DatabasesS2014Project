__author__ = 'jesse'

from CreateIndexes import *


def build_index_analysis():
    btree, btree_loc_to_id, btree_loc_to_id_idx = create_btree_indexes()
