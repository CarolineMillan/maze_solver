from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.__canvas_widget = Canvas(self.__root_widget, bg="white", height=height, width=width)
        self.__canvas_widget.pack(fill=BOTH, expand=1)
        self.__running = False

        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas_widget, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_colour):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2)

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        min_x = min(x1, x2)
        min_y = min(y1, y2)
        max_x = max(x1, x2)
        max_y = max(y1, y2)

        bl = Point(min_x, min_y)
        br = Point(max_x, min_y)
        tl = Point(min_x, max_y)
        tr = Point(max_x, max_y)

        if self.has_left_wall:
            # draw it
            lw = Line(bl, tl)
            self.__win.draw_line(lw, "green")
        if self.has_right_wall:
            rw = Line(br, tr)
            self.__win.draw_line(rw, "red")
        if self.has_top_wall:
            tw = Line(tl, tr)
            self.__win.draw_line(tw, "purple")
        if self.has_bottom_wall:
            bw = Line(bl, br)
            self.__win.draw_line(bw, "orange")
