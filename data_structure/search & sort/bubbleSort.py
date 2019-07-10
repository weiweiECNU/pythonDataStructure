import random
def randomIntList( num ):
    """随机生成包含 num 个整数的数组"""
    alist = []
    for i in range(num):
        alist.append(random.randint(1,50))
    
    return alist

alist = randomIntList(20)

def bubbleSort(alist, acending = True):
    """冒泡排序要对一个列表多次重复遍历。
    它要比较相邻的两项，并且交换顺序排错的项。
    每对 列表实行一次遍历，就有一个最大项排在了正确的位置。

    列 表中最大(按照规定的原则定义大小)的数据是所比较的数据对中的一个，它就会沿着列表一直 后移，直到这次遍历结束。

    第二次遍历开始时，最大的数据项已经归位。现在还剩n-1个待排数据项，即有n-2个要比 较的数据对。
    由于每一次遍历都会使下一个最大项归位，所需要遍历的总次数就是n-1。完成n-1 次遍历之后，最小的数据项一定已经归位，此时不需要再执行其他步骤。
    
    在Python里，可以“同时赋值”。通过“a,b=b,a”的语句就可以让两个赋值语句同时进行 (如图2)。用同时赋值的方法可以用一条语句实现交换操作
    需要遍历的总次数就是n-1。完成n-1 次遍历之后，最小的数据项一定已经归位


    1/2(n2-n)。比较复杂度为O(n2)

    缺点：
    必须要在最终位置找到之前不断交换数据项，所以它经常被认为是最低效的排 序方法。这些“浪费式”的交换操作消耗了许多时间

    优点：
    由于冒泡排序要遍历整个未排好的 部分，它可以做一些大多数排序方法做不到的事
    """

    for round in range(len(alist)-1,0,-1):
        for i in range(round):
            if acending:
                if alist[i] > alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            else:
                if alist[i] < alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]


    return alist

print(bubbleSort(alist,False))


def shortBubbleSort(alist, acending = True):
    """
    短路冒泡排序 short bubble
    尤其是如果在整个排序过程中没有交换，我们 就可断定列表已经排好。
    因此可改良冒泡排序，使其在已知列表排好的情况下提前结束。
    这就是 说，如果一个列表只需要几次遍历就可排好，冒泡排序就占有优势:它可以在发现列表已排好时 立刻结束。"""

    exchange = True
    round = len(alist)-1
    while round > 0 and exchange:
        exchange = False
        for i in range(round):
            if acending:
                if alist[i] > alist[i+1]:
                    exchange = True
                    alist[i], alist[i+1] = alist[i+1], alist[i]
            else:
                if alist[i] < alist[i+1]:
                    exchange = True
                    alist[i], alist[i+1] = alist[i+1], alist[i]
    
    return alist
 
print(bubbleSort(alist,False))

