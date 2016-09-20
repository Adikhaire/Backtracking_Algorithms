import sys
import numpy as np
from collections import Counter
import time
from IPython import display

# override default recursion limit
sys.setrecursionlimit(1000000000)


class NQueens:

    def __init__(self, size_of_board):
        self.size = size_of_board
        self.columns = [] * self.size
        self.num_of_places = 0
        self.num_of_backtracks = 0
        self.conflict_set = {}
        for i in range(self.size):
            self.conflict_set[i] = []


    def place(self, startRow=0):
        """ Backtracking algorithm to recursively place queens on the board
            args:
                startRow: the row which it attempts to begin placing the queen
            returns:
                list representing a solution
        """
        # if every column has a queen, we have a solution

        if len(self.columns) == self.size:
            print('Solution found! The board size was: ' + str(self.size))
            print(str(self.num_of_places) + ' total places were made.')
            print(str(self.num_of_backtracks) + ' total backtracks were executed.')
            print(self.columns)
            return self.columns

        # otherwise search for a safe queen location
        else:
            for row in range(startRow, self.size):
                # if a safe location in this column exist


                if self.isSafe(len(self.columns), row) is True:
                    # place a queen at the location
                    self.columns.insert(len(self.columns),row)
                    self.num_of_places += 1
                    # recursively call place() on the next column
                    return self.place()

                # if not possible, reset to last state and try to place queen
            else:
                # grab the last row to backtrack from

                lastRow = self.conflict_set[len(self.columns)]
                self.num_of_backtracks += 1
                temp = Counter(lastRow)
                lastRow = max(temp,key=temp.get)
                # initialize the variable to intialize valued
                self.conflict_set[len(self.columns)] = []
                pervious_variable = self.columns.pop(lastRow)
                # recursively call place() from the last known good position, incrementing to the next row
                return self.place(startRow = pervious_variable)

    def isSafe(self, col, row):
        """Determines if a move is safe.
        args:
            col: column of desired placement
            row: row of desired placement
            self.columns: list of queens presently on the board
        returns:
            True if safe, False otherwise
        """
        # check for threats from each queen currently on boar
        for threatRow in self.columns:
            # for readability
            threatCol = self.columns.index(threatRow)
            # check for horizontal/vertical threats
            if row == threatRow or col == self.columns.index(threatRow):
                self.conflict_set [col].append(threatCol)
                return False
            # check for diagonal threats
            elif threatRow + threatCol == row + col or threatRow - threatCol == row - col:
                self.conflict_set[col].append(threatCol)
                return False
        # if we got here, no threats are present and it's safe to place the queen at the (col, row)
        return True

# set the size of the board
size = input("Enter the size of the board:")
n = int(size)
# instantiate the board and call the backtracking algorithm
start = time.time()
queens = NQueens(n)
queens.place(0)
stop = time.time()
seconds = stop - start
print("Time required for Execution",seconds*1000)
# convert board to numpy array for pretty printing
board = np.array([[' '] * n] * n)
for queen in queens.columns:
    board[queens.columns.index(queen), queen] = 'Q'

print(board.T)

