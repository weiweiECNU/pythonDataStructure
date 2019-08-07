#括号匹配问题的另一个例子是超文本标记语言(HTML)。
# 在 HTML 中，标记以开始 (opening tag，<tag>)和结束(closing tag，</tag>)的形式存在，它们必须成对出现来正确地描 述 web 文档。
# 这个非常简单的 HTML 文档:只是为了表明语言中标记的匹配和嵌套结构。
# 写一个程序，它可以检查 HTML 文档中是否有匹 配的开始和结束标记。

from stack import Stack
import re

def readHtml(address):
    files = open(address, "r")
    htmlString = files.read()
    files.close()
    
    htmlString = ''.join(htmlString.split())


    return htmlString

def checkRight( label ):
    return label.find("/") != -1

def isMatch(label1, label2):
    return label1 == "/"+label2 or label2 == "/"+label1



#def bracket_matching_html( address ):
address = "stack/sample.html"
htmlString = readHtml(address)
re1 = re.compile(r'[<](.*?)[>]')
lables = re.findall(re1, htmlString)

labelStack = Stack()

matching = True

for label in lables:
    if not checkRight( label):
        labelStack.push( label )
    else:
        if labelStack.size() == 0:
            matching = False
        else:
            if isMatch(label, labelStack.peek()):
                labelStack.pop()
            else:
                matching = False

if labelStack.size() != 0:
    matching = False

print(lables)
print(matching)



        






