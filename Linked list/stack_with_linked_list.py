from unorderedList import UnorderedList

class StackLinkedList:
    def __init__(self):
        '''Stack()创建一个新的空栈。不需要参数，并返回一个空栈'''
        self.items = UnorderedList()     

    def push(self, item):
        '''Push(item)将新项添加到堆栈的顶部。它需要参数 item 并且没有返回值'''
        self.items.add(item)

    def pop(self):
        '''pop()从栈顶删除项目。它不需要参数,返回 item。栈被修改'''
        return self.items.pop()

    def peek(self):
        """返回栈顶的项，不删除它。它不需要参数。堆栈不被修改。"""
        return self.items.index(0)

    def isEmpty(self):
        """测试看栈是否为空。它不需要参数，返回一个布尔值。"""
        return self.items.isEmpty()

    def size(self):
        """返回栈的项目数。它不需要参数，返回一个整数。"""
        return self.items.size()
    
    def __str__(self):
        return str(self.items)