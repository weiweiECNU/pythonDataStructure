from binheap import BinHeap

class PriorityQueue():
    """优先级队列"""
    def __init__(self, maxNode):
        self.priorityQueue = BinHeap( maxNode )
        self.dataDict = dict()

    def enqueue(self, priority, data):
        """入队"""
        self.priorityQueue.insert(priority)
        self.dataDict[priority] = data

    
    def dequeue(self):
        """出队"""
        pri =  self.priorityQueue.delMin()
        return self.dataDict[pri]


a = PriorityQueue(10)
a.enqueue(9,10)
a.enqueue(5,6)
a.enqueue(6,7)
a.enqueue(2,3)
a.enqueue(3,4)
print(a.dequeue())