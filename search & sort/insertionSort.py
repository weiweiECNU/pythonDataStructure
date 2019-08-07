import random
def randomIntList( num ):
    """随机生成包含 num 个整数的数组"""
    alist = []
    for i in range(num):
        alist.append(random.randint(1,100))
    
    return alist

alist = randomIntList(20)
def insertionSort(alist, ascending = True):
    """选择排序提高了冒泡排序的性能它总是保持一个位置靠前的 已排好的子表，然后每一个新的数据项被“插入”到前边的子表里，排好的子表增加一项
   程序第8行是转移操作，即把某个数据放到后一个位置，空出当前位置以待数 据插入。
   关于“转移”与“交换”操作的考虑也很重要。通常情况下，“转移”的步骤约为“交换” 步骤的1/3，因为它只有一次赋值操作
   
   插入排序需要进行的最多的比较次数仍是从1到n-1的所有的整数之和，即复杂度为O(n2)。
   但 是，最好的情况下，每排一个数据只需要一次比较，即列表已经排好的情况。"""

    for index in range( 1, len(alist)):
        valueToInsert = alist[index]
        position = index

        if ascending:
            while position > 0 and alist[position-1] > valueToInsert:
                alist[position] = alist[position-1]
                position -= 1
        else:
            while position > 0 and alist[position-1] < valueToInsert:
                alist[position] = alist[position-1]
                position -= 1

        alist[position] = valueToInsert
    
    return alist

print(insertionSort(alist,ascending= False))     


