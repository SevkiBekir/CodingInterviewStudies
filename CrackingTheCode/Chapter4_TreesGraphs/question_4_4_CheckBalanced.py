from Utils.BinaryTree import BinaryTree
from Utils.BinaryTreeNode import BinaryTreeNode


def isBalanced(rootNode):
    left = getHeight(rootNode.left, 1)
    right = getHeight(rootNode.right, 1)

    if left+1 == right or left == right + 1 or left == right:
        print("The binary tree is balanced")
        return True
    else:
        print("The binary tree is NOT balanced")
        return False

def getHeight(node, height):
    if node is None:
        return height - 1

    left = getHeight(node.left, height+1)
    right = getHeight(node.right, height+1)

    if left > right:
        return left
    else:
        return right


if __name__ == '__main__':
    bt = BinaryTree()

    dataList = [1, 2, 3, 4, 5, 6]
    bt.constructBtWrt(dataList)
    bt.printPreOrder(bt.root)
    isBalanced(bt.root)

    bt2 = BinaryTree()
    bt2_root = BinaryTreeNode(1)
    bt2_root.left = BinaryTreeNode(2)
    bt2_root.left.left = BinaryTreeNode(3)
    bt2_root.left.left.right = BinaryTreeNode(5)
    bt2_root.left.left.left = BinaryTreeNode(4)

    bt2.root = bt2_root
    bt2.printPreOrder(bt2.root)
    isBalanced(bt2.root)
