class Node:
    """每个节点对象必须持有至少两条信息。首先，节点必须包含列 表元素本身。
    我们将这称为该节点的“数据区”(data field)。此外，每个节点必须保持到下一个节 点的引用。
    节点类还包括访问和修改的常用方法:返回节点 数据和引用到下一项。"""

    def __init__(self,data):
        self.data = data
        self.next = None # 节点初始 接地
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNode):
        self.next = newNode



