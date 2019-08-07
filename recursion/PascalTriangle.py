def printTrianle( alist ):
    string = ""
    for i in alist:
        string += str(i)
        string += " "
    print(string)


def pascalTriangle( rowNum ):
    """
    输出Pascal三角形。程序里应接受一个参数来定义三角形的行数
    每行的数字都是由 上一行的对角线数字相加而得

    停止条件: rowNum == 1
    递进： rowNum --
    """
    if rowNum == 1:
        printTrianle([1,1])
        return [1,1]
    else:
        formerList = pascalTriangle(rowNum - 1)
        newList = [0] * (len(formerList) + 1)
        newList[0] = 1
        newList[-1] = 1
        for i in range(1,len(formerList)):
            newList[i] = formerList[i-1] + formerList[i]

        printTrianle(newList)
        return newList

pascalTriangle(10)