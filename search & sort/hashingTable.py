class HashTable:

    def __init__(self):
        """产生一个新的空映射，返回一个空映射的集合。"""
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,val):
        """往映射中添加一个新的密钥-数据值对。如果密钥已经存在，那么将旧的数据 值置换为新的。
        put函 数(见表3)假设最终一定能找到一个能让新的密钥填入的槽，除非它已经在 中存在。 
        基于这样的假设，它能够计算出最初的散列值，如果发现对应的槽不为空时，调用 (rehash)函数直到找到空槽位置。
        如果一个非空的槽已经含有该密钥，那么就将其数据值替换 为当前数据值。
        
        
        散列函数运用的是简单的求余方法。        这里的冲突解决技术是运用“+1”的线性探测。
        
    
        """

        hashvalue = self.hashfunction( key, self.size )

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = val
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] == val      # replace 
            else:
                newHashValue = self.rehash(hashvalue,self.size)
                while self.slots[newHashValue] != None and self.slots[newHashValue] != key:
                    newHashValue = self.rehash(newHashValue,self.size)

                if self.slots[newHashValue] == None:
                    self.slots[newHashValue] = key
                    self.data[newHashValue] = val

                elif self.slots[newHashValue] == key:
                    self.data[hashvalue] == val  # replace

    def hashfunction(self, key, size):
        """散列函数运用的是简单的求余方法。       """
        return key%size

    def rehash(self,oldhash,size):
        """ 这里的冲突解决技术是运用“+1”的线性探测 """
        # 开放地址法：open addressing

        # 线性探测。linear probing
        
        #return (oldhash+1)%size

        # 扩展线性探测 extend the linear probing technique
        # 不再按顺序一个一个地寻找新槽，而是 跳过一些槽，这样能更加平均地分配出现冲突的数据，进而潜在地减少集中问题出现的次数

        return (oldhash+3)%size
        
        #二次探测法quadratic probing
        #我们不是每次在冲突中选择跳过固定个数的槽，而是 使用一个再散列函数使每次跳过槽的数量会依次增加1,3,5,7,9，以此类推。
        #这意味着如果原槽为 第h个，那么再散列时访问的槽为第h+1，h+4，h+9，h+16个，以此类推。换言之，二次探测法 使用一个连续的完全平方数数列作为它的跳跃值。
        


    def get(self, key): 
        """给定一个 key 值，返回关联的数据，若不存在，返回None 。

        首先计算最初的散列值。如果结果不在对应的槽中，再散列 (reshash)函数就会被用来确定一下个可能存储该密钥的位置。
        确保了我们没有再次回到原槽，保证了搜索操作不会陷入死循环。如果这种情况发生了，那么我们已经遍历所有可
        能的槽，这个密钥一定是不存在的。
        
        """
        startHash = self.hashfunction( key, self.size )
        data = None
        found = False
        stop = False

        position = startHash

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data =  self.data[position]
            else:
                position = self.rehash( position, self.size)
                if position == startHash:
                    stop = True
        return data        

    def __getitem__(self,key):
        """我们重载了运算 符__getitem__和__setitem__允许使用“[]”对字典进行访问。
        这表示一旦一个散列表被建立， 我们所熟悉的索引操作符都将是可用的"""
        return self.get(key)
    
    def __setitem__(self, key, data):
        """"""
        self.put(key,data)

    
    def len(self):
        """返回映射中的存储密钥-数据值对的个数"""
        num = 0
        for i in self.slots:
            if i != None:
                num += 1
        return num

    def __contains__(self, key):
        """为散列表实现的ADT Map实现in方法(__contains__)。
        当表述是key in map，返回 True否则返回 False"""
        return self.get(key)



class HashTable2:
    """从一个使用数据项链的方法来解决冲突的hash table"""
    def __init__(self):
        """产生一个新的空映射，返回一个空映射的集合。"""
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,val):
        """往映射中添加一个新的密钥-数据值对。如果密钥已经存在，那么将旧的数据 值置换为新的。
        put函 数(见表3)假设最终一定能找到一个能让新的密钥填入的槽，除非它已经在 中存在。 
        基于这样的假设，它能够计算出最初的散列值，如果发现对应的槽不为空时，调用 (rehash)函数直到找到空槽位置。
        如果一个非空的槽已经含有该密钥，那么就将其数据值替换 为当前数据值。
        
        
        散列函数运用的是简单的求余方法。        这里的冲突解决技术是运用“+1”的线性探测。
        

        在散列表实现的Map中，散列表的大小被定为101。如果散列表被填满，它需要增长。
        重新 实现put方法，使得当负载因子达到某一预定值时(你可以决定这一值基于你对负载与性能 的评估)，散列表会自动调整自身的大小。
    
        """

        hashvalue = self.hashfunction( key, self.size )

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = val
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] == val      # replace 
            else:
                newHashValue = self.rehash(hashvalue,self.size)
                while self.slots[newHashValue] != None and self.slots[newHashValue] != key:
                    newHashValue = self.rehash(newHashValue,self.size)

                if self.slots[newHashValue] == None:
                    self.slots[newHashValue] = key
                    self.data[newHashValue] = val

                elif self.slots[newHashValue] == key:
                    self.data[hashvalue] == val  # replace
        
        # if self.len() > self.size * 0.8:
        #     self.size += 1
        #     self.slots.append(None)
        #     self.data.append(None)


    def hashfunction(self, key, size):
        """散列函数运用的是简单的求余方法。       """
        return key%size

    def rehash(self,oldhash,size):
        """ 这里的冲突解决技术是运用“+1”的线性探测 """
        return (oldhash+1)%size

    def get(self, key): 
        """给定一个 key 值，返回关联的数据，若不存在，返回None 。

        首先计算最初的散列值。如果结果不在对应的槽中，再散列 (reshash)函数就会被用来确定一下个可能存储该密钥的位置。
        确保了我们没有再次回到原槽，保证了搜索操作不会陷入死循环。如果这种情况发生了，那么我们已经遍历所有可
        能的槽，这个密钥一定是不存在的。
        
        """
        startHash = self.hashfunction( key, self.size )
        data = None
        found = False
        stop = False

        position = startHash

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data =  self.data[position]
            else:
                position = self.rehash( position, self.size)
                if position == startHash:
                    stop = True
        return data        

    def __getitem__(self,key):
        """我们重载了运算 符__getitem__和__setitem__允许使用“[]”对字典进行访问。
        这表示一旦一个散列表被建立， 我们所熟悉的索引操作符都将是可用的"""
        return self.get(key)
    
    def __setitem__(self, key, data):
        """"""
        self.put(key,data)


    def delete(self, key):   
        """
                从映射中删除一个密钥-数据值对，声明形式为 del map[key]

    你如何从一个uses chaining for collision resolution的散列表中删除项目?
    如果使用的是open addressing is used的方法呢?
    必须处理的特殊情况是什么?
    实现实现Hashtable类的del方法。

        open addressing is used
        """
        startHash = self.hashfunction( key, self.size )
        stop = False
        position = startHash

        while self.slots[position] != None and not stop:
            if self.slots[position] == key:
                self.data[position] = None
                self.slots[position] = None
            else:
                position = self.rehash( position, self.size)
                if position == startHash:
                    stop = True
                    print("Fail to delect, the key is not found! ")


            

    def len(self):
        """返回映射中的存储密钥-数据值对的个数"""
        num = 0
        for i in self.slots:
            if i != None:
                num += 1
        return num

    def __contains__(self, key):
        """为散列表实现的ADT Map实现in方法(__contains__)。
        当表述是key in map，返回 True否则返回 False"""
        return self.get(key)


H=HashTable2()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H.len())
print( 53 in H)
H.delete(20)

print(H.slots)
print(H.data)
print(H.len())
print( 53 in H)
