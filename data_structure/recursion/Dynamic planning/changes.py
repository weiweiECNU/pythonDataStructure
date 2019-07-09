def recMoneyChange(coinList, change):
    """使用递归的方法 最少的硬币来找零
    我们 要使用面值中最大的硬币(25美分)，并且尽可能多的使用它，接着我们再使用下一个可使用的 最大面值的硬币，也是尽可能多的使用。
    这种方法被称为贪心算法，因为我们试图尽可能快的解 决一个问题。

    基本结束条件： 如果我们要找的 零钱的价值和某一种硬币的价值一样，那么答案很简单，只要一个硬币。
    演进过程：
    我们需要的是一个 1 美分加上给原始价值减去 1 美分找 零所需硬币数量的最小值，
    或者一个 5 美分加上给原始价值减去 5 美分找零所需硬币数量的最小 值，
    或者一个 10 美分加上给原始价值减去 10 美分找零所需硬币数量的最小值，等等。
    所以，给原 始总数找零的硬币数量可以根据下面的方法计算:
    𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠 = 𝑚𝑖𝑛 1 + 𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡 − 1)
     1 + 𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡 − 5) 
     1 + 𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡 − 10)
    { 1 + 𝑛𝑢𝑚𝐶𝑜𝑖𝑛𝑠(𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑎𝑚𝑜𝑢𝑛𝑡 − 25)

    coinList 硬币有哪些面值
    change 需要找的零钱总数

    返回值： 最少的硬币数
    """

    minCoin = change 

    if change in coinList:
        return 1
    else:
        for coin in [ coin for coin in coinList if coin <= change ]:
            newCoin = 1 + recMoneyChange( coinList, change - coin )
            if newCoin < minCoin:
                minCoin = newCoin
    
    return minCoin

#print(recMoneyChange([1,5,10,25],63)) #29.766 seconds


def recMoneyChangeAdvance(coinList, change, knowResults):
    """减少我们的工作量的关键在于记住一些出现过的结果，这样就能避免重复计算我们已经知道 的结果。
    一个简单的解决方案就是我们将所找到的给硬币找零的最小数目存储在一个表中。
    然后 在我们计算一个新的最小值之前，可以先查表看这个结果是否已知。
    如果表中已经有了这个结果，我们就可以从表中引用这个值而不是重复计算
    
    采用的方法还不是动态规划，我们只是使用了一种叫做“函数值缓存”，或者一般称为“缓存”的方法改善了程序的性能。
    """
    minCoin = change 

    if change in coinList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for coin in [ coin for coin in coinList if coin <= change ]:
            newCoin = 1 + recMoneyChangeAdvance( coinList, change - coin , knowResults)
            if newCoin < minCoin:
                minCoin = newCoin
            
        knowResults[change] = minCoin
    
    return minCoin


#print(recMoneyChangeAdvance([1,5,10,25],63,[0]*64))  # 0.045 seconds

def dpMakeChange(coinValueList,change,knowResults):
    """动态规划的解决方法是从为1分钱找零 的最优解开始，逐步递加上去，直到我们需要的找零钱数。
    这就保证了在算法的每一步过程中， 我们已经知道了兑换任何更小数值的零钱时所需的硬币数量的最小值
    
    参数 一个有效 硬币面值的列表、我们想要兑换硬币的数值、一个包含所有部分找零最优解的列表。
    返回 包含从0到所需兑换数值的每一个数值对应的最优解的 list
    """
    for cent in range(change + 1):
        minCoin = cent
        for coin in [ coins for coins in coinValueList if coins <= cent]:
            if knowResults[cent - coin] + 1 < minCoin:
                minCoin = knowResults[cent - coin] + 1
        knowResults[ cent ] = minCoin
    
    return knowResults[cent]

#print(dpMakeChange([1,5,10,25],63,[0]*64)) #0.049 seconds



def dpMakeChangeAdvance(coinValueList,change,knowResults,coinUsed):
    """只要简单的记录我们为knowResults的每一项添加的最后一个硬币面值就可以 了 -> coinUsed
    如果我们知道了最后一个添加的硬币，就可以简单的减去这个硬币的币值来找到最优解列表 中之前的一项进行找零。
    我们可以一直倒退访问列表直到回到列表的最开始。
    
    coinUsed 是一个我们用来找零 的硬币的列表
    """
    for cent in range(change + 1):
        coinCount = cent
        newCoin = 1
        
        for coin in [ coins for coins in coinValueList if coins <= cent]:
            if knowResults[cent - coin] + 1 < coinCount:
                coinCount = knowResults[cent - coin] + 1
                newCoin = coin
        knowResults[ cent ] = coinCount
        coinUsed[ cent ] = newCoin
    
    return knowResults[change]



def printCoins( coinUsed, change ):
    """
    通过重访列表coinUsed，打印出每个使用过的硬币的值。
    """
    coinPrice = change
    while coinPrice > 0:
        coin = coinUsed[coinPrice]
        print(coin)
        coinPrice -= coin


def main():
    amnt = 63
    clist = [1,5,10,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    print("Making change for",amnt,"requires") 
    print(dpMakeChangeAdvance(clist,amnt,coinCount,coinsUsed),"coins") 
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()