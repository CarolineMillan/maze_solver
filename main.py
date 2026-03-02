from graphics import Window, Point, Line, Cell

def main():
    win = Window(800,600)
    p1 = Point(0,0)
    p2 = Point(400, 300)
    line = Line(p1, p2)
    win.draw_line(line, "blue")
    cell1 = Cell(win)
    cell1.draw(50,50,100,100)
    win.wait_for_close()


main()
