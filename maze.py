from cell import Cell
from time import sleep

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        # create a num_cols x num_rows sized 2D array of Cell objects

        self.__cells = [[Cell(self.__win)] * self.__num_rows] * self.__num_cols

        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + (i*self.__cell_size_x)
        x2 = self.__x1 + ((i+1)*self.__cell_size_x)
        y1 = self.__y1 + (j*self.__cell_size_y)
        y2 = self.__y1 + ((j+1)*self.__cell_size_y)
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        sleep(0.05)
