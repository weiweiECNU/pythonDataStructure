from binheap import BinHeap
class BinheapMax(BinHeap):
    """
    二叉堆
    最大堆
    """
    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i//2

    def findMax(self):
        return self.heapList[1]
    
    def findMin(self):
        pass
    
    def delMax(self):
        max = self.heapList[1]
        self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
        self.heapList.pop()
        self.heapSize -= 1
        self.percDown(1)
        return max
    
    def percDown(self, i):
 
        while i * 2 < self.heapSize:
            child = self.maxChild(i)
            if self.heapList[i] < self.heapList[child]:
                self.heapList[i], self.heapList[child] = self.heapList[child], self.heapList[i]
            
            i = child

    
    def maxChild(self, i):

        if i * 2 + 1 > self.heapSize:
            return i * 2
        else:
            child = i * 2 if self.heapList[i*2] > self.heapList[i*2 + 1]  else i*2+1
            return child


bh = BinheapMax()
bh.buildHeap([9,5,6,2,3])

print(bh.delMax()) 
print(bh.delMax()) 
print(bh.delMax()) 
print(bh.delMax()) 
print(bh.delMax())