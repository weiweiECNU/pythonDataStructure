from node import Node

class UnorderedList:
    def __init__(self):
        """每个 UnorderedList 对象将保持列表的头一个节点的引用。"""
        self.head = None
    def isEmpty(self):
        """(判断链表是否为空)方法仅仅只是检查了列表的头是否指向 None, 返回布尔值"""
        return self.head == None

    def add(self,item):
        """增加新节点的地方是在头部
        是把新插入节点的引用设为 原来列表的头节点。
        把列表头部 head 指向这个新的节点。
        31 是添加到列表中的第一项，那么它最终将在链表的最后一个节点，因为之后的 每一项被添加在它前面"""

        temp = Node( item )
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """我们需要遍历链表，并且记录出现过的节点个数 
        外部引用称为“当前”(current), 只要这个外部引用没有遇到列表的尾端(None)，我们就将 current 移动到下一个节点，"""

        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """每当我们访问一个链表中的节点时，我们会判断储存在此的数据是否就是我们所要找的元素。
        然而在这个例子中，我们并没有 必要遍历整个列表。
        事实上，如果我们的工作进行到了列表的底端，这意味着我们所要寻找的元素 在列表中并不存在。
        同样，如果我们找到了那个元素，那么就没有必要继续寻找了。
        """

        current = self.head
        found = False
        while (not found) and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self, item):
        """在遍历链表时使用两个外部引用。current 不变，仍然标记当前遍历到 的位置。
        新加入的引用——我们叫“前一个”(   )——在遍历过程中总是落后于 current 一 个节点。
        这样，当 current 停在待删除节点时，   即停在链表中需要修改的节点处。"""

        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() != item:
                previous = current
                current = current.getNext()
            else:
                found = True
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext( current.getNext() )
        
    def append(self,item):
        """在队尾加  O(n)"""
        current = self.head
        while current.getNext() != None:
            current = current.getNext()

        temp = Node(item)
        current.setNext( temp )

    def insert(self, index, item):
        current = self.head
        previous = None
        count = 0
        while count < index:
            count += 1
            previous = current
            current = current.getNext()
        
        temp = Node(item)
        temp.setNext(current)

        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)
            

    def index(self,index):
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.getNext()
        
        return current.getData()
    
    def pop(self):
        """在队头删去 """
        data = self.head.getData()
        self.head = self.head.getNext()
        return data


    def print(self):
        """从头到尾打印列表"""
        current = self.head
        while current != None:
            print( current.getData())
            current = current.getNext()

    def __str__(self):
        """字符串形式的表现"""
        current = self.head
        string = ""
        while current != None:
            string += str(current.getData())+" -> "
            current = current.getNext()

        string += "None"
        return string 
    
    def slice(self, start, stop):
        """无序列表的切片方法。它包含 start 和 stop 两个参数，
        返回一个从 start 位置开始向后到 stop 位置但不包含 stop 位置的列表的副本。"""
        current = self.head
        count = 0
        # backup = UnorderedList()
        # while count < stop:
        #     if count >= start:
        #         backup.add(current)
        #     count += 1
        #     current = current.getNext()
        # return backup

        backup = []
        while count < stop:
            if count >= start:
                backup.append(current.getData())
            count += 1
            current = current.getNext()
        
        backupList = UnorderedList()
        for i in backup:
            backupList.add(i)
        return backupList

        


            
        
        
