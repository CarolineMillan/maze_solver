from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        self.canvas_widget = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas_widget.pack(fill=BOTH, expand=1)
        self.running = False

        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.canvas_widget, fill_colour)

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
