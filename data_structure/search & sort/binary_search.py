def binary_search(alist, item):
    """二分搜 索将从中间项开始检测，而不是按顺序搜索列表。
    如果查找项与我们刚搜索到的项匹配，则搜索 结束。如果不匹配，我们可以利用列表的有序性来排除掉一半的剩余项。
    如果查找项比中间项大，我们可以把列表中较小的那一半全部和中间项可以从接下来的考察中排除了。
    因为如果查找 项在列表中，那它一定在较大的那一半。
    
    接下来，我们可以在较大的一半中重复这个过程。从中间项开始，拿它和查找项作比较。
    再 来一次，我们要么找到了查找项，要么从中间分割列表，并因此排除掉另一大部分我们的搜索区 域。
    
    分割次数 项数
    1       n/2
    2       n/4
    3       n/8
    ...
    i       n/2^i

    n/2^i = 1
    i = log2(n)

    二分搜索的复杂度是O(log(n))
    

    """

    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and found != True:
        mid = (first + last) //2
        if item == alist[mid]:
            return True
        elif item > alist[mid]:
            first = mid + 1
        else:
            last = mid - 1
        
    return False

alist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]

#print(binary_search(alist,8))



def binary_search_RC(alist,item):
    """分而治之，递归实现 二分查找
    停止条件： len(list) == 0
    递进过程： 判断 alist[mid] ?= item
            if item < alist[mid]:
                binary_search_RC(alist[:mid],item)
            else:
                binary_search_RC(alist[mid+1:],item)

    """

    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            return binary_search_RC(alist[:mid],item)
        else:
            return binary_search_RC(alist[mid+1:],item)
        



def binary_search_RC_advance(alist,item,first,last):
    """分而治之，递归实现 二分查找
    停止条件： len(list) == 0
    递进过程： 判断 alist[mid] ?= item
            if item < alist[mid]:
                binary_search_RC(alist[:mid],item)
            else:
                binary_search_RC(alist[mid+1:],item)

    用递归算法实现二分搜索，避免用切片操作。切片操作花费时间长
    记得，对子列表传递的除了列表外，还要有 开始以及结束位置在列表中的索引值。
    通过一个随机产生的有序整数列表来与课件中采用 切片操作的二分搜索比较性能

    """

    if first == last:
        return False
    else:
        mid = (first + last) // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
            return binary_search_RC_advance(alist,item,first,last)
        else:
            first = mid + 1
            return binary_search_RC_advance(alist,item,first,last)


import random
from timeit import Timer


def randomSortedIntList( num ):
    """随机生成包含 num 个有序整数的数组"""
    alist = []
    for i in range(num):
        alist.append(random.randint(1,50))
    
    return alist

alist = randomSortedIntList(20)



t1 = Timer("binary_search_RC(alist, 3)","from __main__ import binary_search_RC")

t2 = Timer("binary_search_RC_advance(alist,3,0,len(alist)-1)","from __main__ import binary_search_RC_advance")

print("",t1.timeit(number=1000),"milliseconds")
print("",t1.timeit(number=1000),"milliseconds")

# print(binary_search_RC(alist,3))
