# from pythonds.basic.stack import Stack
# from pythonds.trees.binaryTree import BinaryTree

# 1.扩展 buildParseTree 函数，使它能够解决没有空格分隔的数学表达式。
# 2.修改 buildParseTree 函数和 evaluate 函数，用它们解决布尔表达式(与 and，或 or 和非 not) 。记住非是一个一元操作符，这会让你的编程稍稍复杂一点。

from node_list import BinaryTree
from stack import Stack
import operator
import re
from traversal import printexp
from traversal import inorder

def buildParseTree(fexp):
    """如果当前读入的字符是 '(' ,添加一个新的节点(node)作为当前节点的左子节点，当前节点下降。
    如果当前读入的字符在列表 ['+','-','/','*'] 中，将当前节点的根值设置为当前读入的字符。添加 一个新的节点(node)作为当前节点的右子节点，当前节点下降。
    如果当前读入的字符是一个数字，将当前节点的根值设置为该数字，当前节点变为它的父节点 (parent)。
    如果当前读入的字符是 ')' ，当前节点变为其父节点(parent)。


    在构建解析树的过程中我们需要保持对当前节点和其父节点的追踪
    一个简单的方法就是利用堆栈在遍历整个树的过程中保持 对父节点的跟踪。
    每当我们要下降到当前节点的子节点时，我们先将当前节点压入栈中。
    而当我们 想要返回当前节点的父节点时，我们就能从堆栈中弹出该父节点。

"""
    charList = fexp.replace(" ","")
    btree = BinaryTree("")
    eStack = Stack()
    digits = ""
    # logisics = ""
    # logisFlag = False
    digitFlag = False
    currentTree = btree
    eStack.push(currentTree)
    for char in charList:
        if char.isdigit():
            digits += char
            digitFlag = True
        # if char.isalpha():
        #     logisics += char
        #     logisFlag = True
        else:
            if digitFlag:
                currentTree.setRootVal(int(digits))
                parent = eStack.pop()
                currentTree = parent
                digits = ""
                digitFlag = False
            
            # if logisFlag:
            #     currentTree.setRootVal(logisics)
            #     parent = eStack.pop()
            #     currentTree = parent
            #     logisics = ""
            #     logisFlag = False

            if char == "(":
                currentTree.insertLeft("")
                eStack.push(currentTree)
                currentTree = currentTree.getLeftChild()
        
            elif char in ["+","-","*","/"]:
                currentTree.setRootVal(char)
                currentTree.insertRight("")
                eStack.push(currentTree)
                currentTree = currentTree.getRightChild()
            
        # elif char.isdigit():#char in ["1","2","3","4","5","6","7","8","9","0"]: #Python isdigit() 方法检测字符串是否只由数字组成。
        #     currentTree.setRootVal(int(char))
        #     parent = eStack.pop()
        #     currentTree = parent
        
            elif char == ")":
                parent = eStack.pop()
                currentTree = parent

            else:
                raise ValueError
        
    return btree


def evaluate(parseTree):
    """写一个函数来计算解析树 的值，并返回该计算结果
    
    递归计算表达式值的函 数。
    这个递归算法的最小基本问题是检查一个操作符是否为叶节点
    如果左右子节点的值都是 None,那么我们就能知道这个当前节点是一个叶节点。
    我们返回这个叶节点存储的数值作为求值的结果即可
    
    使函数朝向基本情形前进的递归过程就是调用 函数获取当前节点的左子 树、右子树的值。递归调用使我们有效地朝叶节点移动
    如果当前节点不是一个叶节点
    ，我们只需简单地使储存在父节点中的操作符应用到两 个子节点返回的运算结果上

    字典里的值是 Python 的操作符模块(operator module)中的函数。这个操作符模块为我们提供了很多 常用操作符的函数
    operator.add operator.sub operator.mul operator.truediv

    """

    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftTree = parseTree.getLeftChild()
    leftRight = parseTree.getRightChild()
    if leftTree and leftRight:
        fn = opers[ parseTree.getRootVal() ]
        return fn(evaluate(leftTree), evaluate(leftRight))

    else:
        return parseTree.getRootVal()


pt = buildParseTree("((15+5)* 3 )")
# a ="( ( 10 + 5 ) * 3 )"
# b = a.split()
# c = a.replace(" ","")
# print(b)
# print(c)

# for char in b:
#     print(char)
# for char in c:
#     print(char)

#print(evaluate(pt))
inorder(pt)
print(printexp(pt))