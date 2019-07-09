from node import Node

class OrderedList:
    def __init__(self): 
        self.head = None

    def isEmpty(self):
        """(判断链表是否为空)方法仅仅只是检查了列表的头是否指向 None, 返回布尔值"""
        return self.head == None

    def add(self,item):
        """我们需要遍历链表来寻找 添加新节点的位置。
        遍历时，当我们遍历完了整个列或者当前节点的值大于我们要添加的值时，
        我 们就找到了添加新节点的位置。"""

        current = self.head
        previous = None
        stop = False

        while current != None and  not stop:
            if current.getData() > item:
                stop = True 
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        temp.setNext(current)

        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

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
        一旦当前节点的值大于我们要找的值，我们就可以停止搜索并返回 False
        """

        current = self.head
        found = False
        stop = False
        while (not found) and current != None and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True 
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

    def index(self,index):
        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.getNext()
        
        return current.getData()
    
    def pop(self):
        """在队头删去 """
        self.head = self.head.getNext()

    def print(self):
        """从头到尾打印列表"""
        current = self.head
        while current != None:
            print( current.getData())
            current = current.getNext()
    
