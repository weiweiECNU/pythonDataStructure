from binarySearchTree import BinarySearchTree
from treeNode import TreeNode

class avlTreeNode(TreeNode):
    def __init__(self, key, val, balanceFactor = 0, left = None, right = None , parent = None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0
    

    


class avlTree(BinarySearchTree):

    def _put(self, key, value, currentNode):
        """"""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent= currentNode)
                self.updataBalance(currentNode.leftChild)

        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent= currentNode)
                self.updataBalance(currentNode.rightChild)


        else: 
            currentNode.replaceNodeData( key, value, left = currentNode.leftChild, right = currentNode.rightChild)

    
    def updataBalance(self, node):
        """更新节点的 平衡因子
        如果当前节点需要再平衡， 那么只需要对当前节点进行再平衡， 而不需要进一步更新父节 点。
        如果当前节点不需要再平衡， 那么父节点的平衡因子需要调整。 如果父节点的平衡因子非 零，
        那么算法通过父节点递归调用 updateBalance 方法继续往上传递到树的根。
        
        first checks to see if the current node is out of balance enough to require rebalancing (line 16). 

        If that is the case then the rebalancing is done and no further updating to parents is required. 

        If the current node does not require rebalancing then the balance factor of the parent is adjusted. 

        If the balance factor of the parent is non-zero then the algorithm continues to work its way up the tree 
        toward the root by recursively calling updateBalance on the parent."""

        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance( node )
        
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif  node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updataBalance(node.parent)

    def rebalance(self, node):
        """1. 如果子树需要左旋转使之平衡， 首先检查右节点的平衡因子。 如果右节点左重则右节点做 右旋转，然后原节点左旋转。
                2. 如果子树需要右旋转使之平衡， 首先检查左节点的平衡因子。 如果左节点右重然后左节点 左旋转，然后原节点右旋转。
        """
        # 右重 左旋转
        if node.balanceFactor < -1:
            if node.rightChild.balanceFactor > 1:
                self.rotateRight( node.rightChild)

            self.rotateLeft( node )
        elif node.balanceFactor > 1:
            if node.leftChild.balanceFactor < -1:
                self.rotateLeft(node.leftChild)
            self.rotateRight(node)
                
    def rotateRight(self, rotRoot):
        """右旋转"""
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            elif rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
        
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
    
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(0, rotRoot.balanceFactor)
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(0, newRoot.balanceFactor)
        
    def rotateLeft(self, rotRoot):
        """执行一个左旋转我们需要做到以下几点: 
        1. 使右节点(B)成为子树的根。
        2. 移动旧根(A)到新根的左节点。
        3. 如果新根 (B) 原来有左节点， 那么让原来 B 的左节点成为新根左节点 (A) 的右节 点。
        注:由于新根(B)是 A 的右节点，在这种情况下移动后的 A 的右节点一定是空的。这使得我 们不用多想就可以直接给移动后的 A 添加右节点。

        为了维持二叉搜索树的所有 性质，必须以绝对正确的顺序把节点移来移去。此外，我们需要确保正确地更新了所有的 parent 指 针。

        右节点已经被存储在这个临时变量。我们将旧根的右节点替换 为新根的左节点。
        下一步是调整两节点的父指针。如果新根 newroot 原来有左节点，左节点的新父节点变成老 根。新根的父节点将成为旧根的父节点。
        如果旧根是整个树的根，那么我们必须让整棵树的根指向 这个新的根。否则，如果旧的根是左节点，那么我们改变左节点的父节点到一个新的根;
        否则，我 们改变右节点的父节点到一个新的根(行 10-13) 。最后我们设置的旧根的父节点成为新的根
        """

        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot

        newRoot.parent = rotRoot.parent

        if rotRoot.isRoot():
            self.root = newRoot 
        else:
            if rotRoot.isLeftChild(): 
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot

        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)
        







