
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):    
        """在队首插入一个元素，参数为待插入元素，无返回值"""
        self.items.append(item)
    
    def addRear(self,item):
        """在队尾插入一个元素，参数为待插入元素，无返回值"""
        self.items.insert(0, item)
    
    def removeFront(self):
        """在队首移除一个元素，无参数，返回值为该元素。双端队列会被改变。"""
        return self.items.pop()
    
    def removeRear(self): 
        """在队尾移除一个元素，无参数，返回值为该元素。双端队列会被改变。"""
        return self.items.pop(0)

    def isEmpty(self): 
        """判断双端队列是否为空，无参数，返回布尔值。"""
        return self.items == []
    
    def size(self):
        """返回双端队列中数据项的个数，无参数，返回值为整型数值"""
        return len(self.items)
    
    def __str__(self):
        return self.items

