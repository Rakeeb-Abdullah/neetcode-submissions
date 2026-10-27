class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_seen={i:set() for i in range(9)}
        square_seen={(i//3,j//3):set() for i in range(9) for j in range(9)}

        for i in range(9):
            row_seen=set()
            
            for j in range(9):
                c=board[i][j]
                if c!=".":

                    if c in row_seen or c in column_seen[j] or c in square_seen[(i//3,j//3)]:
                        return False
                    

                    row_seen.add(c)
                    column_seen[j].add(c)
                    square_seen[(i//3,j//3)].add(c)

        
        return True
