from Utils.BinaryTree import BinaryTree

if __name__ == '__main__':
    sortedList = [1,2,3,4,5,6]

    bst = BinaryTree()
    bst.constructBstWith(sortedList)
    bst.printPreOrder(bst.root)
