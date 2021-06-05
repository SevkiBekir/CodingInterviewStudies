from Utils.BinaryTree import BinaryTree
from Utils.BinaryTreeNode import BinaryTreeNode

if __name__ == '__main__':
    bt = BinaryTree()

    dataList = [1,2,3,4,5,6]
    bt.constructBtWrt(dataList)
    bt.printPreOrder(bt.root)

    data = bt.getDepthLinkedLists()
    for linkedlist in data.items():
        linkedlist[1].printList()


    bt2 = BinaryTree()
    bt2_root = BinaryTreeNode(1)
    bt2_root.left = BinaryTreeNode(2)
    bt2_root.left.left = BinaryTreeNode(3)
    bt2_root.left.left.right = BinaryTreeNode(5)
    bt2_root.left.left.left = BinaryTreeNode(4)

    bt2.root = bt2_root
    bt2.printPreOrder(bt2.root)
    data = bt2.getDepthLinkedLists()
    for linkedlist in data.items():
        linkedlist[1].printList()