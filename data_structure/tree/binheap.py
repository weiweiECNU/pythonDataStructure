class BinHeap:
    """二叉堆
    一个实现优先队列的经典的方法便是采用二叉堆(Binary Heap)数据结构。二叉堆能将优先队列 的入队和出队复杂度都保持在 O(logn).。
    二叉堆的有趣之处在于，其逻辑结构用图形表示很像二叉树，但我们却可以仅仅用一个列表来 实现它。
    二叉堆通常有两种:最小成员 key 排在队首的称为“最小堆(min heap)”，反之，最大 key 排在队首的是“最大堆(max heap)
    这个是最小堆

    “完全二叉树”的结构来近 似实现“平衡”。完全二叉树，指每个内部节点都有两个子节点，最多可有一个节点例外
    另一个有趣的特性是我们能用单个列表来实现完全树而不需要使用节点，引用或嵌套 列表。
    因为对于完全树，如果节点在列表中的位置为 p，那么其左子节点的位置为 2p，类似的，其 右子节点的位置为 2p+1
    若节点在列表中的位置为 n，那么父节点的位置是 n//2

    堆的次序性 我们用来在堆里储存数据项的方法依赖于维持堆次序。
    所谓堆次序，是指堆中任意一个节点 x，其父节点 p 中的 key 均小于或等于 x 中的 key

    """
    # 6. 实现一个大小有限的二叉堆。也就是说，这个堆仅仅保存 n 个优先级最高的数据项。如 果堆的大小即将超过 n，最不重要的节点将被丢弃。

    def __init__(self, maxNode):
        """创建一个新的空二叉堆对象
        其中表首下标为 0 的项并没有用到，但为了后面代码可以用到简单的整数乘除 法，仍保留它。
        """
        self.heapList = [0]
        self.heapSize = 0
        self.maxNode = maxNode

    def insert(self, k):
        """加入一个新数据项到堆中
        通过比较新加入的数据项和父节点的方法来恢复堆的次序性。如果新加入的数据项比父节点要 小，可以把它与父节点互换位置。
        一系列交换操作来使新加入的数据项“上浮”到正 确位置。
        
        新加入的数据的位置就是 heapsize
        """
        
        self.heapList.append(k)
        self.heapSize += 1
        self.percUp(self.heapSize)
        if self.heapSize > self.maxNode:
            self.heapList.pop()
            self.heapSize -= 1

    def percUp(self, i):
        """上浮函数
        当我们让一个数据项“上浮”时，我们保证了新节点与父节点以及其他兄弟节点之间的堆次序
        如果新节点非常小，我们可能仍需要把它向上交换到另一个层级。事实上，我们需要不断交 换，直到到达树的顶端。
        将当前节点的下标除以 2，我们就能计算出任何节点的父节点。
        """
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    def findMin(self):
        """返回堆中的最小项,最小项仍保留在堆中 """
        return self.heapList[1]

    def delMin(self):
        """返回堆中的最小项,同时从堆中删除
        比较困难的是移走根节点的数据项后如何恢复堆结构和堆次 序。我们可以分两步走。
        首先，用最后一个节点来代替根节点。移走最后一个节点维持了堆结构的 性质。如此简单的替换，还是可能破坏堆次序。
        这就要用到第二步:将新节点“下沉”来恢复堆次序。 图 6.18 所示是一系列交换操作来使新节点“下沉”到正确位置
        
        """
        least = self.heapList[1]
        self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
        self.heapList.pop()
        self.heapSize -= 1
        self.percDown(1)
        return least


    def percDown(self, i):
        """下降函数
        为了维持堆的次序性，我们只需要交换根节点和比根节点小的最小子节点。
        首次交换后，我们 可能需要不断循环交换过程，直到新的根节点比两个子节点都小
        """
        while i * 2 < self.heapSize:
            child = self.minChild(i)
            if self.heapList[i] > self.heapList[child]:
                self.heapList[i], self.heapList[child] = self.heapList[child], self.heapList[i]
            
            i = child

    
    def minChild(self, i):
        """返回最小子节点
        对于完全树，如果节点在列表中的位置为 p，那么其左子节点的位置为 2p，类似的，其 右子节点的位置为 2p+1。
        """
        if i * 2 + 1 > self.heapSize:
            return i * 2
        else:
            least = i * 2 if self.heapList[i*2] < self.heapList[i*2 + 1]  else i*2+1
            return least

    def isEmpty(self):
        """返回堆是否为空"""
        empty = True if self.heapList == 0 else False
        return empty

    def size(self):
        """返回堆中数据项的个数"""
        return self.heapSize

    def buildHeap(self, alist):
        """从一个 key 列表创建新堆
        有关二叉堆的最后一部分便是找到方法从无序表生成一个“堆”。我们最自然的想法是:用 insert (key)方法，将无序表中的数据项逐个插入到堆中。
        对于一个排好序的列表，我们可以用二分搜索 找到合适的位置来插入下一个 key，操作复杂度是 O(logn).
        然而插入一个数据项到列表中间需要将列 表其他数据项移动为新节点腾出位置，操作复杂度是 O(n).
        因此用 insert(key)方法的总代价是 O(nlogn)。其实，我们能直接将整个列表生成堆，将总代价控制在 O(n)。
        
        完整地加载无需表
        从树中间开始，然后回溯到根节点，percDown 方法保证了最大子节点总是 “下沉”。
        
        """
        self.heapList = [0] + alist[:]
        self.heapSize = len(alist)

        for i in range( len(alist)//2 ,0,-1):
            self.percDown(i)
        
        if self.heapSize > self.maxNode:
            for i in range(self.heapSize - self.maxNode):
                self.heapList.pop()
                self.heapSize -= 1

    # def heapsort(self, alist):
    #     self.heapList = [0] + alist[:]
    #     self.heapSize = len(alist)

    #     for i in range( len(alist),0,-1):
    #         self.percDown(i)
        


    #     return 

# bh = BinHeap(4)
# bh.buildHeap([9,5,6,2,3])

# print(bh.delMin()) 
# print(bh.delMin()) 
# print(bh.delMin()) 
# print(bh.delMin()) 
