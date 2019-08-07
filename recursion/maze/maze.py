import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, mazefile):

        self.mazelist = []

        mazeFile = open(mazefile,"r")
        rowsInMaze = 0
        for line in mazeFile:
            rowlist = []
            column = 0
            for ch in line:
                rowlist.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = column
                column += 1
            rowsInMaze += 1
            self.mazelist.append( rowlist )
            columnsInMaze = len(rowlist)
        
        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        #turtle.addshape("orange.gif")
        #self.t = turtle.Turtle(shape='orange.gif')
        self.t = turtle.Turtle(shape='turtle')
        turtle.setup(width=600,height=600)
        turtle.setworldcoordinates(-(columnsInMaze-1)/2-.5,
                            -(rowsInMaze-1)/2-.5,
                            (columnsInMaze-1)/2+.5,
                            (rowsInMaze-1)/2+.5)

    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,y-y+self.yTranslate,'black')
        
        self.t.color('black','blue')


    def drawCenteredBox(self,x,y,color):
        turtle.tracer(0)
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color('black',color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
            self.t.end_fill()
        turtle.update()
        turtle.tracer(1)

myMaze = Maze('mazemap.txt')
myMaze.drawMaze()
