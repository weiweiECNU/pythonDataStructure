def balance(fromStr, toStr):
    if len(fromStr) > len(toStr):
        toStr += " "*(len(fromStr) - len(toStr))
    elif len(fromStr) < len(toStr):
        fromStr += " "*(len(toStr) - len(fromStr))
    
    return fromStr, toStr

def funcname(fromStr, toStr  ):
    """这个问题叫做单词最小编辑距离问题，在很多领域的研究中起到了很大作用。
    假设你想把单 词“algorithm”变为“alligator”。

    对于每一个字母，你有三种变换方式:
    从源单词复制一个字母到目 标单词，计5分;
    从源单词删除一个字母，计20分;
    在目标单词插入一个字母，计20分。

    最后将 一个单词转换为另一个的分数可以被拼写检查系统使用，用来给彼此相似的单词提供建议。
    使用 动态规划技术，写一种算法得到任何两个单词之间的最小编辑距离。
    
    单元格中的值是什么?
    如何将这个问题划分为子问题? 
    网格的坐标轴是什么?

    在动态规划中，你要将某个指标最大化
    单元格中的值通常就是你要优化的值 : 最小编辑距离
    需要比较子串
    坐标轴很可能是这两个单词的字母

    https://www.cnblogs.com/robert-dlut/p/4077540.html  
    """
    # fromStr,toStr = balance(fromStr,toStr)
    delectScore = 20
    addScore = 20
    pasteScore = 5

    dp = [ [ 0 for _ in range(len(toStr)) ] for _ in range(len(fromStr))] 

    for j in range(len(toStr)):
        for i in range(len(fromStr)):
            if i == 0 or j == 0:
                dp[i][j] = 20*(i + j)
            else:
                delect = dp[i][j-1] + delectScore
                add = dp[i-1][j] + addScore
                paste = dp[i-1][j-i]  if fromStr[i] == toStr[j]  else dp[i-1][j-1] + pasteScore
                dp[i][j] = min( delect, add, paste )

    return dp[ len(fromStr)-1][len(toStr)-1]


    
print(funcname("abc","abcd"))


