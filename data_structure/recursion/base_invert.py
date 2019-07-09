def to_str(n, base):
    """
     递归算法必须有个基本结束条件
     递归算法必须改变自己的状态并向基本结束条件演进 
     递归算法必须递归地调用自身
    
    将原始整数分解为一连串的单个数字。 
    2)通过在字符序列中检索将单个数字转换成字符串。 
    3)将这些单个数字的字符串连接起来，形成最终的结果。

    基本结束条件 : 当 n 小于 base 时
    向基本结束条件演进: 整数的除法取余的运算
    """
    convert_string = "0123456789ABCDEF"

    if n < base:
        return convert_string[n]
    else:
        return to_str( n//base  , base) + convert_string[ n % base]
    

print(to_str(16,2))

def reserveString( string ):
    """递归 反向字符串
    基本结束条件 : 字符串长度为1
    向基本结束条件演进: 字符串 Slice 和 连接
    """
    
    reserve = ""
    if len(string) == 1:
        reserve += string
        return reserve 
    else:
        reserve += string[0] 
        return reserveString(string[1:]) + reserve

print(reserveString("a"))

    
