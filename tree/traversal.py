from node_list import BinaryTree

#前序遍历(preorder):在前序遍历中，我们先访问根节点，然后递归地前序遍历访问左子树，再 递归地前序遍历访问右子树。
#中序遍历(inorder):在中序遍历中，我们递归地中序遍历访问左子树，然后访问根节点，最后 再递归地中序遍历访问右子树。
#后序遍历(postorder):在后序遍历中，我们先递归地后序遍历访问左子树和右子树，最后访问 根节点。

def preorder(atree):
    """用递归来编写"""
    if atree:
        print(atree.getRootVal())
        preorder(atree.getLeftChild())
        preorder(atree.getRightChild())

#内置和外置这两种方法哪种更好一些呢?一般来说外置函数更好。
# 原因在于你很少需要单纯遍 历整个树。多数情况下你只是想利用基本的遍历方法来实现其他的事情。

def postorder(atree):
    """后序遍历"""
    if atree:
        preorder(atree.getLeftChild())
        preorder(atree.getRightChild())
        print(atree.getRootVal())

#后序遍历的一种一般应用，也就是解析树求值


def inorder(atree):
    """中序遍历"""
    if atree:
        preorder(atree.getLeftChild())
        print(atree.getRootVal())
        preorder(atree.getRightChild())

# 7.整理 printexp 函数，使其不包括多余的括号。
def printexp(atree):
    """我们对解析树进行一个简单的中序遍历，我们将得到没有圆括号的原始表达式。
    我们可以 修改基础的中序遍历的算法使我们复原全括号表达式。
    只要做如下修改:在递归访问左子树之前输 出左括号，然后在访问右子树之后输出右括号。"""
    sVal = ""

    if atree:
        left =  atree.getLeftChild()
        right = atree.getRightChild()
        if not left and not right: # 树叶节点，都是数字
            sVal += str(printexp(left))
            sVal += str(atree.getRootVal())
            sVal += str(printexp(right))

            
        
        
        else:
            sVal += "("+ printexp(left)
            sVal += atree.getRootVal()
            sVal += printexp(right) + ")"
    return sVal
