class TreeNode:
    """TreeNode类提供了许多辅助函数，使BinarySearchTree类的方法更容易做到
    属性： 
    key     键 排序的依据
    value   值
    leftchild 左子节点
    rightchild 右子节点
    parent    父节点
    """

    def __init__(self, key, val, left = None, right = None , parent = None ):
        """有时我们想要创建一个新的TreeNode带有一 个父节点和一个子节点。就现存的父节点和子节点，我们可以把它们作为参数。
        其余时候我们只会 创建一个带键-值对的TreeNode，而不传入任何参数。在这种情况下，我们使用可选参数的缺省值"""

        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent.leftChild == self and self.parent

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.leftChild and not self.rightChild

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


    def replaceNodeData(self, key, val, left, right):
        """替换 Node """
        self.key = key 
        self.value = val 
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        else:
            self.rightChild.parent = self

    def findSuccessor(self):
        """利用二 叉搜索子树的中序遍历，按从最小到最大打印出子树中的节点。寻找继任者有三种情况需要考虑:
1. 如果节点有右子节点，那么继任者是在右子树中最小的键。
2. 如果节点没有右子节点，是其父节点的左子节点，那么父节点是继任者。
3. 如果节点是其父节点的右子节点，而本身无右子节点，那么该节点的继任者是其父节点的继任 者，不包括这个节点。
当从二叉搜索树中删除节点时，第一种情况是唯一对我们重要的"""
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.rightChild = None 
                succ = self.parent.findSuccessor() 
                self.parent.rightChild = self
        return succ


    def findMin(self):
        """找到一个子树中的最小键。要相信，最小值在任何二叉搜索子树中都是子树的 左子树。
        因此 findMin 方法只简单地追踪左子树，直到找到没有左子树的叶节点。"""
        minNode = self
        while self.hasLeftChild():
            minNode = minNode.leftChild
        
        return minNode

    def spilceOut(self):
        """移动继任者"""
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
    
    def __iter__(self):
        """假设我们想要按顺序简单地遍历树上所有的 键值。这是我们用字典所做能的事，为什么不在树也实现呢?
        我们已经知道如何使用中序遍历二叉 树，然而，写一个迭代器需要更多一点的工作，因为每次调用迭代器时，一个迭代器只返回一个节点。
        Python提供了一个非常强大的函数yield，使用时创建一个迭代器。yield和return相似，它也返回 一个值给调用者。
        yield也有额外的步骤来记住函数运行目前的状态，以便下次调用函数时，继续从当 前状态执行。创建可迭代对象的函数被成为生成器。
        
        二叉树的中序迭代器代码如代码6.43所示。仔细看看这个代码:乍一看，你可能会认为代码是非 递归的。但是请记住，__iter__ 重写 for x in   的操作符来实现迭代，所以它确实是递归!因为它是对TreeNode进行递归，   在
        TreeNode类中定义。"""
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
