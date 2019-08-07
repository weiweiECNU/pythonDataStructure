# a tree represented by a list of list
# 嵌套列表法的一个非常好的特性是子树的结构与树相同;
# 这个结构本身是递 归的!子树具有一个根值和两个表示叶节点的空列表。
# 嵌套列表法的另一个优点是它容易扩展到多 叉树。
#
#

def BinaryTree(r):
    """构建包含一个根节点和两个表示子节点的空列表的列表"""
    return [r,[],[]]

def insertLeft(root, newBranch):
    """给左子树添加到树 的根，我们需要插入一个新的列表到根列表的第二个位置。
   如果列表中已经有元素 在第二个位置，我们需要跟踪它，并将新节点插入树中作为其左子节点
    If the list already has something in the second position, 
    we need to keep track of it and push it down the tree as the left child of the list we are adding
    
    我们首先应获取对应于当前左子节点的列表(可能是空的)。 
    然后，我们添加新的左子节点，将原来的左子结点作为新节点的左子节点。这使我们能够将新节点 插入到树中的任何位置。
    
    root  树的根或者是某个节点
    newBranch 新插入的子树
    """

    t = root.pop(1)  
    if len(t) > 1:   # 如果已经有元素的话，len 为3
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root, newBranch):
    """给右子树添加到树的根，我们需要插入一个新的列表到根列表的第三个位置"""
    t = root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    """返回 树 的 根节点 内容"""
    return root[0]

def setRootVal(root,newVal):
    """更改树根节点内容"""
    root[0] = newVal
    
def getLeftChild(root):
    """
    """
    return root[1]

def getRightChild(root):
    """
    """
    return root[2]


r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)  # 这是浅拷贝 浅拷贝仅仅复制了容器中元素的地址. l 改变之后 r 也跟着改变
                    # 深拷贝是 b=deepcopy(a) 
print(l)
setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)



n = BinaryTree("a")
insertLeft(n,"b")
insertRight(n,"c")
insertRight(getLeftChild(n),"d")
insertLeft(getRightChild(n),"e")
insertRight(getRightChild(n),"f")

print(n)
