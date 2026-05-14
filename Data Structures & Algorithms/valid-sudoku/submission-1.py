class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows
        for i in board:
            checklist = [0]*10
            for j in i:
                if j == ".":
                    pass
                elif checklist[int(j)] != 0:
                    return False
                else:
                    checklist[int(j)] += 1
        #cols
        for i in range(0,9,1):
            checklist = [0]*10
            for j in range(0,9,1):
                k = board[j][i]
                if k == ".":
                    pass
                elif checklist[int(k)] != 0:
                    return False
                else:
                    checklist[int(k)] += 1

        #boxes
        for k in range(0,9,1):
            checklist = [0]*10                
            for i in range(3*(k%3),3 + 3*(k%3),1):
                for j in range(3*(k//3),3 + 3*(k//3),1):
                    x = board[i][j]
                    if x == ".":
                        pass
                    elif checklist[int(x)] != 0:
                        return False
                    else:
                        checklist[int(x)] += 1

        return True
                    



        