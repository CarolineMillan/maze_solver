from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)
    #p1 = Point(0,0)
    #p2 = Point(400, 300)
    #line = Line(p1, p2)
    #win.draw_line(line, "blue")
    #cell1 = Cell(win)
    #cell1.draw(50,50,100,100)
    #cell2 = Cell(win)
    #cell2.draw(150,150,200,200)
    #cell3 = Cell(win)
    #cell3.draw(250,250,300,300)
    #cell1.draw_move(cell2)
    #cell2.draw_move(cell3, True)
    maze = Maze(5,5,20,20,50,50,win)
    win.wait_for_close()


main()
