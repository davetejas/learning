"""
Problem : Build merkel tree by adding one leave at a time

Tree properties / assumptions :
- balanced binary tree
- lowest lvl reflects all the leaves(data)
- no restriction to size or height of the tree
- Implementation only supports Insert operation

"""
import sys
import hashlib


def bld_hash(data):
    data = repr(data).encode('utf-8')
    hs = hashlib.md5(data)
    return hs.hexdigest()

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.mhash = None    # holds cypto_hash for sub tree


class Leaf(Node):
    def __init__(self):
        self.data = None


def bld_leaves(data_list):
    leaves = []
    for i in data_list:
        lv_node = Leaf()
        lv_node.data = i
        lv_node.mhash = bld_hash(i)
        leaves.append(lv_node)
    print('list of leaves -> {}'.format(leaves))

    return leaves


def bld_parent(left, right):

    if left is None and right is None:
        AssertionError("Invalid bld elem")

    parent = Node()
    parent.left = left
    parent.right = right
    parent.mhash = bld_hash(left.mhash + right.mhash)
    return parent


"""
A recursive implementation to bld tree from bottom up.

inputs as list of children for each lvl

- builds even number of leaves by adding dummy data to make tree balanced
"""

def update_mtree(leaves):

    entries = len(leaves)

    if entries == 1:
        root = leaves[0]
        return root                     # this breaks recursion

    parent_list = []
    i = 0
    while i < entries:
        left = leaves[i]
        if i+1 < entries:
            right = leaves[i+1]
        else:
            empty_lv = [0]               # 0 is just dummy data to cal hash
            right = bld_leaves(empty_lv) # insert empty node to make it balanced

        p = bld_parent(left, right)
        parent_list.append(p)
        i += 2

        print("parent hash : {} <- left_child {} -> right_child {} ".format(p.mhash, left.mhash, right.mhash))

    # recursive call
    update_mtree(parent_list)


# Can be implemented for append to tree

# def traverse_mtree(node):
#     print(node.data)
#     if node.left is None or node.right is None:
#         return node
#     if node.left:
#         traverse_mtree(node.left)
#     if node.right:
#         traverse_mtree(node.right)


if __name__ == '__main__':
    insert_list = list()
    elems = input("Enter number of elements to add to merkle tree:")

    for i in range(int(elems)):
        print("{}th element:".format(i+1))
        e = input()
        insert_list.append(int(e))

    print(insert_list)

    leaves = bld_leaves(insert_list)

    res = update_mtree(leaves)


