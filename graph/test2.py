n = int(input())

for i in range(n):
    x,y =  map(int, input().split())
    if i == 0:
        xLargest = x
        xSmall = x
        yLargest = y
        ySmall = y
    else:
        if x > xLargest:
            xLargest = x
        if x < xSmall:
            xSmall = x
        if y > yLargest:
            yLargest = y
        if y < ySmall:
            ySmall = y

xLength = xLargest-xSmall
yLength = yLargest-ySmall


if xLength > yLength:
    print(xLength ** 2 )
else:
    print(yLength ** 2)
