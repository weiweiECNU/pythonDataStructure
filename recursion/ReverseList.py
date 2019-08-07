def reverseList( alist ):
    """ 写一个递归函数来反转一个列表。

    基本结束条件 : list 长度为1
    演进: list 最后一个元素 + 去掉最后元素后剩下的 元素组成的 list (list 的长度递减)
    """

    if len(alist) == 1:
        return alist
    else:
        return [alist[-1]] + reverseList(alist[:-1])

#extend 向列表尾部追加一个列表，将列表中的每个元素都追加进来，在原有列表上增加
# + 直接用+号看上去与用extend()一样的效果，但是实际上是生成了一个新的列表存这两个列表的和，只能用在两个列表相加上
#a=[1,2,3]
#b=[9,8,7]

#test=a.extend(b)
#print(a)        #[1, 2, 3, 9, 8, 7]
#print(test)     #None

# test=a+b
# print(a)        #[1, 2, 3]
# print(test)     #[1, 2, 3, 9, 8, 7]

# += 效果与extend()一样，向原列表追加一个新元素，在原有列表上增加
# a+=b
# print(a)        #[1, 2, 3, 9, 8, 7]

print(reverseList(list("abcdedfg")))
