#############
#我们将模拟这个问题的方法是 编写一个函数，该函数生成一个 27 个字符长度的字符串，从 26 个字母和空格中随机选择一个字符。
# 我们将编写另一个函数，来比较随机生成的字符串和目标字符串。
# 第三个函数将反复调用生成和比较函数，那么如果所有目标字母都在随机字符串中出现了，我 们就完成了。
# 如果字母没有全部出现，我们会生成一个全新的字符串.为了让它更易于跟随你的程序 的过程，
# 第三个函数应该返回出到目前为止产生的最好的字符串，并返回在产生这个字符串之前每 1000 次尝试中产生其它不合题意的字符串的次数。
import random 
import string


def generate(size):
    """
    该函数生成一个 27 个字符长度的字符串，从 26 个字母和空格中随机选择一个字符。
    """
    #seed = string.ascii_lowercase + string.digits

    seed = string.ascii_lowercase + " "

    return ''.join([random.choice(seed) for i in range(size)])


def compare( str1, str2 ):
    """
    比较随机生成的字符串和目标字符串。
    字符串长度相同
    """
    counter = 0
    if len(str1) != len(str2):
        return False, counter
    else:
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                counter += 1
        
        if counter != len(str1):
            return False, counter
        else:
            return True,counter


def unlimited_monkey( target ):
    """
    反复调用生成和比较函数，那么如果所有目标字母都在随机字符串中出现了，我 们就完成了。
    如果字母没有全部出现，我们会生成一个全新的字符串.为了让它更易于跟随你的程序 的过程，
    第三个函数应该返回出到目前为止产生的最好的字符串，并返回在产生这个字符串之前每 1000 次尝试中产生其它不合题意的字符串的次数。
    """
    candidate = generate(len(target))
    while compare( candidate , target ) == False:
        candidate = generate(len(target))
        print(candidate)

    return candidate

print(compare("empty","emptu"))


######挑战
#看看你是否可以这样优化程序，保留正确的字母，只修改符合到目前为止与目标字符串最接近 的字符串中的一个字符。
#如果新生成的字符是目标字符串中需要的，我们就用这个字符覆盖前一个 字符串中不合题意的字符，这是一种类似“爬坡”的算法。