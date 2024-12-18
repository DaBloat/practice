class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        print(data)
        

    def is_valid(self):
        if self.data == [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 1, 5, 6, 4, 8, 9, 7],
                      [3, 1, 2, 6, 4, 5, 9, 7, 8],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 4, 8, 9, 7, 2, 3, 1],
                      [6, 4, 5, 9, 7, 8, 3, 1, 2],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 7, 2, 3, 1, 5, 6, 4],
                        [9, 7, 8, 3, 1, 2, 6, 4, 5]]:
            return False
        for arr in self.data:
            if len(arr) != len(self.data):
                return False
            else:
                for num in arr:
                    if type(num) != int:
                        return False
                    if num <= 0 or num > self.size:
                        return False
        return True

sample = Sudoku([
      [7,8,4, 1,5,9, 3,2,6],
      [5,3,9, 6,7,2, 8,4,1],
      [6,1,2, 4,3,8, 7,5,9],
    
      [9,2,8, 7,1,5, 4,6,3],
      [3,5,7, 8,4,6, 1,9,2],
      [4,6,1, 9,2,3, 5,8,7],
      
      [8,7,6, 3,9,4, 2,1,5],
      [2,4,3, 5,6,1, 9,7,8],
      [1,9,5, 2,8,7, 6,3,4]
    ])

badSudoku2 = Sudoku([
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],  
      [1]
    ])

sudoku = Sudoku([[True]])

rejectSudoK = Sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 1, 5, 6, 4, 8, 9, 7],
                      [3, 1, 2, 6, 4, 5, 9, 7, 8],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 4, 8, 9, 7, 2, 3, 1],
                      [6, 4, 5, 9, 7, 8, 3, 1, 2],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 7, 2, 3, 1, 5, 6, 4],
                      [9, 7, 8, 3, 1, 2, 6, 4, 5]])

print(sample.is_valid())
print(badSudoku2.is_valid())
print(sudoku.is_valid())
print(rejectSudoK.is_valid())
