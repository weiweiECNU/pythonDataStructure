# https://www.jianshu.com/p/ef78cc3cad24 动态规划问题集合

def backpack( backWeight, weightList, valueList):
    """
    动态规划写一个函数，来帮助你获得最多价值的宝物。
    你可以利用下面的例子来编写程序:假设你的背包可以容纳的总重量为20，你有如下5件宝物:
    item weight value 
    0 2 3 
    1 3 4 
    2 4 8 
    3 5 8 
    4 9 10
    """
    itemSelected = []
    dp = [ [ 0 for _ in range( backWeight + 1) ]  for _ in range( len(weightList) ) ] 

    for item in range( len(weightList) ):
        for weight in range(1, backWeight + 1):
            if  weight >= weightList[item]:
                dp[item][weight] = max(dp[item-1][weight], dp[item-1][weight - weightList[item]] + valueList[item])
            else:
                dp[item][weight] = dp[item-1][weight]
    
    reserveWeight = backWeight
    for item in range( len(weightList)-1, 0 , -1 ):
        if dp[item][reserveWeight] > dp[item - 1][reserveWeight]:
            itemSelected.append(item)
            reserveWeight -= weightList[item]
    
    return dp[len(weightList)-1][backWeight],itemSelected


            


def main():

    weightList = [2,3,4,5,9]
    valueList = [3,4,8,8,10]
    backWeight = 20
    print(backpack(backWeight,weightList, valueList))


main()