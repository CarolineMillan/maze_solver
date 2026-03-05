import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_zeroes(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            0,
            num_rows,
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_maze_break_entrace_and_exit(self):
        num_cols = 12
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[11][15].has_bottom_wall,
            False,
        )
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__reset_cells_visited()
        for col in m1._Maze__cells:
            for cell in col:
                self.assertEqual(
                    m1._Maze__cells[0][0].visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()
