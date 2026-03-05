from cell import Cell
from time import sleep
from random import seed, randrange

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed is None:
            self.__seed = None
        else:
            self.__seed = seed(seed)
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        # create a num_cols x num_rows sized 2D array of Cell objects

        self.__cells = [[Cell(self.__win) for _ in range(self.__num_rows)] for _ in range(self.__num_cols)]

        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        # draws the ij'th cell in the maze
        x1 = self.__x1 + (i*self.__cell_size_x)
        x2 = self.__x1 + ((i+1)*self.__cell_size_x)
        y1 = self.__y1 + (j*self.__cell_size_y)
        y2 = self.__y1 + ((j+1)*self.__cell_size_y)
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        # adding sleep and redrawing slows things down so it looks animated
        if self.__win != None:
            self.__win.redraw()
            sleep(0.01)

    def __break_entrance_and_exit(self):
        # breaks the entrance and the exit to the maze
        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1
        if len(self.__cells) == 0:
            return
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)

    def __break_walls_r(self, i, j):
        # recursively breaks walls between adjacent cells to turn the grid into a maze
        
        if len(self.__cells) == 0:
            return
        
        self.__cells[i][j].visited = True

        while True:
            to_be_visited = []

            # check adjacent cells, make sure they exist
            if (i > 0) and (self.__cells[i-1][j].visited == False):
                to_be_visited.append([i-1, j, "left"])
            if (i < self.__num_cols - 1) and (self.__cells[i+1][j].visited == False):
                to_be_visited.append([i+1, j, "right"])
            if (j < self.__num_rows - 1) and (self.__cells[i][j+1].visited == False):
                to_be_visited.append([i, j+1, "bottom"])
            if (j > 0) and (self.__cells[i][j-1].visited == False):
                to_be_visited.append([i, j-1, "top"])

            # check to see if there's anywhere we can visit
            if len(to_be_visited) == 0:
                # draw the current cell
                self.__draw_cell(i, j)
                return
            
            next_cell = randrange(len(to_be_visited))

            next_i, next_j, direction = to_be_visited[next_cell]
            
            # knock down the wall between the current cell and the chosen cell
            match direction:
                case "left":
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[next_i][next_j].has_right_wall = False
                case "right":
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[next_i][next_j].has_left_wall = False
                case "bottom":
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[next_i][next_j].has_top_wall = False
                case  "top":
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[next_i][next_j].has_bottom_wall = False
                
            self.__draw_cell(i, j)

            # move to the chosen cell
            self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
        # marks all cells' visited fields as false
        for column in self.__cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        # returns true if the maze was solved, false otherwise
        return self.__solve_r(0,0)

    def __solve_r(self, i, j):
        # a depth first search solution
        self.__animate()
        
        if len(self.__cells) == 0:
            return
        
        self.__cells[i][j].visited = True

        # if we're at the exit cell, return true, we've solved it!
        if (i == self.__num_cols - 1) and (j == self.__num_rows - 1):
            return True

        # recursively check all other directions

        # left
        if (i > 0) and (self.__cells[i-1][j].visited == False) and (self.__cells[i][j].has_left_wall == False):
            next = self.__cells[i-1][j]
            # draw a move
            self.__cells[i][j].draw_move(next)
            solved = self.__solve_r(i-1, j)
            if solved:
                return True
            else:
                self.__cells[i][j].draw_move(next, undo=True)

        # right
        if (i < self.__num_cols - 1) and (self.__cells[i+1][j].visited == False) and (self.__cells[i][j].has_right_wall == False):
            next = self.__cells[i+1][j]
            # draw a move
            self.__cells[i][j].draw_move(next)
            solved = self.__solve_r(i+1, j)
            if solved:
                return True
            else:
                self.__cells[i][j].draw_move(next, undo=True)

        # bottom
        if (j < self.__num_rows - 1) and (self.__cells[i][j+1].visited == False) and (self.__cells[i][j].has_bottom_wall == False):
            next = self.__cells[i][j+1]
            # draw a move
            self.__cells[i][j].draw_move(next)
            solved = self.__solve_r(i, j+1)
            if solved:
                return True
            else:
                self.__cells[i][j].draw_move(next, undo=True)

        # top
        if (j > 0) and (self.__cells[i][j-1].visited == False) and (self.__cells[i][j].has_top_wall == False):
            next = self.__cells[i][j-1]
            # draw a move
            self.__cells[i][j].draw_move(next)
            solved = self.__solve_r(i, j-1)
            if solved:
                return True
            else:
                self.__cells[i][j].draw_move(next, undo=True)

        return False

