from treeNode import TreeNode
class BinarySearchTree:
    """如果左子树中键值 Key 都小于父节点，而右子树中键值 Key 都大于父节点，我 们将这种树称为 BST 搜索树
    这种属性适用于每 个父节点和子节点。所有在左子树的键值是小于根的键值的，所有的键值在右子树均大于根。

    实现二叉搜索树，我们将使用节点和引用方法

    第 一个类我们称为BinarySearchTree，第二个类我们称之为TreeNode。BinarySearchTree类有一个引用指 向TreeNode即二叉搜索树的根


    """

    def __init__(self):
        """创建和使用一个空二叉搜索树"""
        self.root = None
        self.size = 0

    def length(self):
        return self.size


    def __len__(self):
        return self.size

    # def __iter__(self):
    #     return self.root.__iter__()

    def put(self, key, value):
        """写put方法以创建二叉搜索树
        
        检查树是否已经有根节点。如果没有，put将创建一个新 的 并把它作为树的根节点，作为子树的根。
        如果一个根节点已经到位，我们就调用辅助功能_put按下列算法来搜索树"""

        if self.root:
            self._put(key, value, self.root)

        else:
            self.root = TreeNode(key, value)

        self.size += 1
    
    def _put(self, key, value, currentNode):
        """从树的根开始搜索，比较新的键值，如果新的键值是小于当前点。搜索左子 树，如 果新的键值是大于当前节点，搜索右子树。
            当无左(或右)子树的搜索，我们发现的位置就是应该在子树中安装新节点的位置。 向树添加一个节点，在上一步发现插入对象的位置创建一个新的TreeNode。
        """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent= currentNode)

        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent= currentNode)

        else: 
            currentNode.replaceNodeData( key, value, left = currentNode.leftChild, right = currentNode.rightChild)


    def __setitem__(self, key, value):
        """重载[ ]作为操作符，通过添加 __setitem__的方法来调用 put方法。
        这使我们能够编写比如myZTiptree['plymouth’] = 55446一样的python语句，这看上去就像 Python字典。"""

        self.put(key, value)

    def get(self, key):
        """给定键实现对值的检索。get方法比put更容易，
        因为它递归地 搜索子树，直到发现无匹配的叶节点或找到一个匹配的键。
        当一个匹配的键被发现后，存储在节点 的值被返回。"""

        if self.root:
            val = self._get(key, self.root)
            if val:
                return val
        
        else:
            return None

    def _get(self, key, currentNode):
        """ 方法的搜索代码，使用_put方法中选择左或右子节点的逻辑。请注意，使用_get方法返回一个 给get，这使得_get成为一个灵 活的辅助方法，"""
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            self._get(key, currentNode.leftChild)
        else:
            self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        """实施__getitem__方法，我们可以写若干Python语句，使它们看起来就像我们访问字典一 样，而事实上我们只是在用一个二叉搜索树，
        例如Z = myziptree [ 'fargo’]。如你可以看到，所有的 __getitem__方法都是调用get"""
        return self.get(key)

    def __contains__(self, key):
        """ 写 方法从而能够使用操作符in。 会简单的调用get，当 返回值的时候就返回 true  ，如果get返回None就返回False。"""
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self, key):
        """首要任务是找 到要删除的搜索树的节点。如果树有一个以上的节点，我们使用_get方法搜索找到需要删除的 TreeNode;
        如果树只有一个节点，这意味着我们要移除树的根，但是我们仍然必须检查以确保根的键 是否匹配要删除的键。
        在以上两种情况下，如果未发现键值，del操作符就会报错。"""
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1 
        else:
            raise KeyError("Error, key not in tree")

    def remove(self, currentNode):
        """
        删除节点，并调整二叉搜索树
        要删除的节点没有子树：
        如果当前节点没有子树，所有我们需要做的是删除该节 点并把指向该节点的引用移动给其父节点。
        
        删除有两个子树的节点
        如果一个节点有两个子节点，我们不可能简单 地其中一个作为提升至父节点的位置，这就需要寻找一个节点，用来代替一个计划删除的节点，
        我 们需要的这个节点，需要保存现有的左、右子树以及二叉搜索树关系。符合该要求的节点有树中第 二大的键。
        我们称这个节点为继任者，然后我们将一路寻找继任者，继任者保证没有一个以上的子节点，所以我们知道如何用已经知道的两种情况实现它。
        一旦继任者被移动，我们把它放在将被删除的子节点处。
       
       我们是用辅助方法 findSuccessor和findMin来找到继任者 的。而移动继任者，我们利用方法spliceOut。
       我们用  spliceOut 的原因是它能帮助我们直接找到需要分 割的节点，做出正确的变化。
       
       
        删除有一个子树的节点
        第二种情况只是稍微复杂(参见代码6.40)。如果一个节点只有一个子节点，那我们可以提升子 树以代替其父树的位置。
        你看这段代码，就会看到有六种情况考 虑。由于有一个左或右子树的情况是对称的，我们将只讨论在当前节点有左子树的情况下，然后做对称。决策过程如下:
            1.如果当前节点是左子节点，那我们只需要更新当前节点的左子节点指向当前节点的父节点引 用，然后将父节点对左子节点的引用更新到当前节点的左子节点。
            2.如果当前节点是一个右子节点，那我们只需要更新当前节点的左子节点指向当前节点的父节点引 用，然后将父节点对右子节点的引用更新到当前节点的左子节点。
            3.如果当前节点没有父树节点，它必须是根节点。在这种情况下，我们只需更换键，有效载荷， 左子节点和右子节点，方法是调用根节点的replaceNodeData方法

        """
        if currentNode.isLeaf():   #没有子树
            if currentNode.parent.hasLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        
        elif currentNode.hasBothChildren(): # 有两个子树
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload


        else: # 有一个子树
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.value, currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.value, currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)



# 3.使用 findSuccessor 方法，写一个二叉搜索树的非递归的前序遍历。
# 4. 修改二叉搜索树的代码使其成为链式的。写一个链式的二叉搜索树的非递归的前序遍历 方法。
# 一个链式的二叉搜索树中，每个节点只有对其后继的引用(即没有 parent 这个参量 —译者注)

