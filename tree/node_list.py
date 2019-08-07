class BinaryTree:
    """定义具有根值，以及左子树 和右子树属性的类。
    
    重要的是要记住这种 方式通过是 left 和 right 属性引用其他 BinaryTree 类实现的。
    例如，当我们插入一个新的左子节点到 树中时，我们创建了另一个的实例，并修改了根节点的 self.leftChild 使之指向新的树"""

    def __init__(self, val):
        self.key = val
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        """第一种情况的特征是，没有现有左子节点。
        当没有左子节点 时，简单地将新节点添加到树中即可。
        第二种情况的特征是，当前存在左子节点。
        在第二种情况 下，我们插入一个节点并将已存在的子节点降级"""

        if self.leftChild:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp
        
    def insertRight(self,newNode):
        if self.rightChild:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key
    
    def preorder(self):
        """前序遍历"""
        print(self.getRootVal())
        if self.getLeftChild():
            self.getLeftChild().preorder()
        if self.getRightChild():
            self.getLeftChild().preorder()
    
    def postorder(self):
        """后序遍历"""
        if self.getLeftChild():
            self.getLeftChild().preorder()
        if self.getRightChild():
            self.getLeftChild().preorder()
        print(self.getRootVal())



# 让我们生成 一个简单的树

# atree = BinaryTree("a")
# atree.insertLeft("b")
# atree.getLeftChild().insertRight("d")
# atree.insertRight("c")
# atree.getRightChild().insertLeft("e")
# atree.getRightChild().insertRight("f")

# print(atree.getRootVal())
# print(atree.getLeftChild().getRootVal())
# print(atree.getRightChild().getRootVal())
# print(atree.getLeftChild().getRightChild().getRootVal())
# print(atree.getRightChild().getLeftChild().getRootVal())
# print(atree.getRightChild().getRightChild().getRootVal())
