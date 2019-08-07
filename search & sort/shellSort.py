import random
def randomIntList( num ):
    """随机生成包含 num 个整数的数组"""
    alist = []
    for i in range(num):
        alist.append(random.randint(1,100))
    
    return alist

alist = randomIntList(20)

def shellSort(alist,ascending = True):
    """
    它以插入排序为基础，将原来要排序的列表划分为一 些子列表，再对每一个子列表执行插入排序，从而实现对插入排序性能的改进。
    划分子列的特定 方法是希尔排序的关键。我们并不是将原始列表分成含有连续元素的子列，而是确定一个划分列 表的增量“i”，
    这个i更准确地说，是划分的间隔。然后把每间隔为i的所有元素选出来组成子列 表。

    然这个 列表还没有完全排好序，但有趣的是，经过我们对子列的排序之后，列表中的每个元素更加靠近 它最终应该处在的位置。

    你可能会觉得希尔排序不会比插入排序要好，因为它最后一步执行了一次完整的插 入排序。
    但事实上，最后的一次排序并不需要很多次的比对和移动，因为正如上面所讨论的，这 个列表已经在之前的对子列的插入排序中实现了部分排序。
    换句话说，每个步骤使得这个列表与 原来相比更趋于有序状态。这使得最后的排序非常高效。

    我们可以说 它的时间复杂度大致介于O(n)和O(n2)之间
    通 过改变间隔的大小，比如以2k-1(1,3,5,7,15,31等等)为间隔，希尔排序的时间复杂度可以达到 O(n3/2)。

    通过调用插入排序实现
    """

    increment = len(alist) // 2
    
    while increment > 0:
        for startPosition in range( increment ):
            alist = gapInsertionSort(alist, startPosition, increment,ascending)

        print("After increments of size",increment, "The list is",alist)
        increment = increment // 2

def gapInsertionSort(alist,startPosition,increment,ascending):
    """
    有间隔的 插入排序
    """
    for index in range( startPosition+increment, len(alist), increment):
        valueToInsert = alist[index]
        position = index

        if ascending:
            while position >= increment and alist[position-increment] > valueToInsert:
                alist[position] = alist[position-increment]
                position -= increment
        else:
            while position >= increment and alist[position-increment] < valueToInsert:
                alist[position] = alist[position-increment]
                position -= increment

        alist[position] = valueToInsert
    
    return alist

print(alist)
shellSort(alist)