from graphics import Point, Line

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_x = max(x1, x2)
        max_y = max(y1, y2)

        tl = Point(min_x, min_y)
        tr = Point(max_x, min_y)
        bl = Point(min_x, max_y)
        br = Point(max_x, max_y)

        if self.__win == None:
            return

        lw = Line(bl, tl)
        rw = Line(br, tr)
        tw = Line(tl, tr)
        bw = Line(bl, br)
        if self.has_left_wall:
            self.__win.draw_line(lw, "black")
        else:
            self.__win.draw_line(lw, "white")
        if self.has_right_wall:
            self.__win.draw_line(rw, "black")
        else:
            self.__win.draw_line(rw, "white")
        if self.has_top_wall:
            self.__win.draw_line(tw, "black")
        else:
            self.__win.draw_line(tw, "white")
        if self.has_bottom_wall:
            self.__win.draw_line(bw, "black")
        else:
            self.__win.draw_line(bw, "white")

    def get_center(self):
        return Point((self.__x2 + self.__x1)/2, (self.__y2 + self.__y1)/2)

    def draw_move(self, to_cell, undo=False):
        center1 = self.get_center()
        center2 = to_cell.get_center()
        line = Line(center1, center2)

        if self.__win == None:
            return
        
        if undo:
            self.__win.draw_line(line, "gray")
        else:
            self.__win.draw_line(line, "red")
