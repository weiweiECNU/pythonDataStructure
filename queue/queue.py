class Queue:
    """设定队列的队尾在列表的 0 位置。"""
    def __init__(self):
        """创建一个空队列对象，无需参数，返回空的队列"""
        self.queue = []

    def enqueue(self, item):
        """将数据项添加到队尾，无返回值;"""
        self.queue.insert(0,item)

    def dequeue(self):
        """从队首移除数据项，无需参数，返回值为队首数据项;"""
        return self.queue.pop()

    def isEmpty(self):
        """测试是否为空队列，无需参数，返回值为布尔值;"""
        return self.queue == []
  
    def size(self):
        """返回队列中的数据项的个数，无需参数。"""
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

