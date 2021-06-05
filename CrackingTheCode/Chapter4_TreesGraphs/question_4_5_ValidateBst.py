import sys

from Utils.BinaryTree import BinaryTree
from Utils.BinaryTreeNode import BinaryTreeNode


def checkBst(binaryTree):
    maxInf = sys.maxsize
    minInf = -sys.maxsize - 1

    leftRange = [minInf,binaryTree.root.data]
    rightRange = [binaryTree.root.data,maxInf]

    leftTree = isNodeInRange(binaryTree.root.left,leftRange)
    rightree = isNodeInRange(binaryTree.root.right,rightRange)

    result = leftTree and rightree

    if result:
        print("The tree is BST")
    else:
        print("The tree is NOT BST")


    return result


def isNodeInRange(node, range):
    if node is None:
        return True


    left = isNodeInRange(node.left,range)
    right = isNodeInRange(node.right,range)

    nodeResult = node.data >= range[0] and node.data <= range[1]

    return nodeResult and left and right


if __name__ == '__main__':
    bt = BinaryTree()

    dataList = [1, 2, 3, 4, 5, 6]
    bt.constructBtWrt(dataList)
    bt.printPreOrder(bt.root)

    checkBst(bt)

    bt2 = BinaryTree()

    bt2_root = BinaryTreeNode(15)

    bt2_root.left = BinaryTreeNode(10)
    bt2_root.left.left = BinaryTreeNode(5)
    bt2_root.left.right = BinaryTreeNode(12)
    bt2_root.left.left.right = BinaryTreeNode(6)
    bt2_root.left.left.left = BinaryTreeNode(2)

    bt2_root.right = BinaryTreeNode(25)
    bt2_root.right.left = BinaryTreeNode(22)
    bt2_root.right.right = BinaryTreeNode(30)
    bt2_root.right.left.right = BinaryTreeNode(23)
    bt2_root.right.left.left = BinaryTreeNode(21)

    bt2.root = bt2_root

    bt2.printPreOrder(bt2.root)

    checkBst(bt2)