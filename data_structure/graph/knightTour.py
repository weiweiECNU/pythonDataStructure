from pythonds import Graph

def knightGraph( size ):
    """在每个格子上 knightGraph 函数调用 genLegalMoves 辅助函数来创建一个当 前这个格子上骑士所有合法移动的列表。
    所有的合法移动都被转换为图上的边。"""
    knightGrh = Graph()
    for row in range(size):
        for col in range(size):
            location = posToNodeId( row, col, size )
            legalList = genLegalMoves( row, col, size)
            for legal in legalList:
                legal_loc = posToNodeId(legal[0], legal[1], size)
                knightGrh.addEdge(location, legal_loc)

    return knightGrh


def posToNodeId(x, y, size):
    """posToNodeId 根据棋盘上位置的行列信息转换成一个线性顶点数"""
    return x * size + y


def genLegalMoves(x, y, size):
    """获取骑士当前的位置并生成所有八个走棋步"""
    legalList = []
    potencialMove = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i in potencialMove:
        xNew = x + i[0]
        yNew = y + i[1]

        if posIsLegal(xNew, yNew, size):
            legalList.append((xNew,yNew))

    return legalList

def posIsLegal(x, y, size):
    if x >= 0 and x < size and y >= 0 and  y < size:
        return True
    else: 
        return False


def knightTour(n, path, u, limit): 
    """函数 需要四个传递参量: n，当前树的深度; path ，这个节点前所有已访问的 点的列表;   u，我们能够探索的点; limit，搜索总深度限制。
    该函数递归使用:当 knightTour被调用时，首先检查基础状态:如果 path 包含有 64 个节点，函数 knightTour 返回 Done  表示已 经找到一条可周游的路径;
    如果 path 还不够长，我们选择一个新节点并以此为参数调用自身。

    DFS 算法还需要使用“颜色”来追踪图中哪些节点已经被访问过了。未访问的节点染为白色， 访问过的染为灰色。
    如果当前节点的全部邻居节点都被访问且没有达到访问全部 64 个节点，我们 就到了一条死路，这时我们需要回溯。
    回溯机制在 knightTour 返回 False 时启动(即递归的终止 条件)。在 BFS 里面我们用 queue(队列)来跟踪要访问的节点，
    而在 DFS 里由于我们使用了递归，也即默认使用了 Stack(栈)来实现我们的回溯机制。
    当我们从 knightTour 函数返回 False 时 ( line11)，我们依然在 while 循环里面并在 nbrList 中寻找下一个要搜索的节点。
    
    
    
    骑士周游问题高度依赖于你选择顶点搜索先后次序的方法
    当前实现的骑士周游算法是一个时间复杂度为指数 O(kN)的算法
    ，骑士可移动位置的多少取决于骑士在棋盘中的位置。
    我们可以通过计点的平均分枝因 子来估计节点总数。需要注意的是这个算法是指数增长的: k(N+1)-1， k 是棋盘上的平均分枝因子。
    """

    u.setColor("gray")
    path.append(u)
    if n < limit: # 未到达所有节点
        neighbourList = list(n.getConnections())
        i = 0
        done = False
        while not done and i < len(neighbourList):
            if neighbourList[i].getColor() == "white":
                done = knightTour(n+1, path, neighbourList[i], limit)
                i += 1

        if not done:  # 回溯机制在 knightTour 返回 False 时启动(即递归的终止 条件)
            path.pop()
            u.setColor("white")
    
    else: # 包含有 64 个节点，函数 knightTour 返回 Done  表示已 经找到一条可周游的路径
        done = True

    return done 


    # 这一行保证了我们下一步选择有最少可能移动位置的顶点被访问的方格。
    # 选择有最多可能移动位置的节点作为下一个顶点的问题在于骑士将倾向于在周游的早期访问棋 盘中间的方格。当这样的事情发生的时候，骑士将容易被困在棋盘的一边而不能到达棋盘另一边未被访问的方格。
    # 另一方面，首先去访问最少可能的格子会迫使骑士早早的进入边角的格子。 进而保 证骑士早早访问那些不容易到达的角落，并且在需要的时候通过中间的方格跳跃着穿过棋盘
    # 用 这种先验的知识来改进算法性能的做法，称作为“启发式规则”heuristic