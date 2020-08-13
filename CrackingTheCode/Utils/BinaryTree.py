
from Utils.BinaryTreeNode import BinaryTreeNode
from Utils.Tree import Tree


class BinaryTree(Tree):
    def __init__(self):
        super().__init__()

    def constructBstWith(self, sortedList):
        self.root = self._sortedListToBst(sortedList)
        print("BST from SortedList was created")


    def _sortedListToBst(self,sortedList):
        if not sortedList:
            return None

        listSize = len(sortedList)
        mid = int(listSize/2)
        leftNode = self._sortedListToBst(sortedList[:mid])
        root = BinaryTreeNode(sortedList[mid])
        rightNode = self._sortedListToBst(sortedList[mid+1:])

        root.left = leftNode
        root.right = rightNode

        return root

    def printPreOrder(self, node):
        if not node:
            return
        
        print(node.data)
        self.printPreOrder(node.left)
        self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if not node:
            return

        self.printPreOrder(node.left)
        self.printPreOrder(node.right)
        print(node.data)

    def printInOrder(self, node):
        if not node:
            return

        self.printPreOrder(node.left)
        print(node.data)
        self.printPreOrder(node.right)
