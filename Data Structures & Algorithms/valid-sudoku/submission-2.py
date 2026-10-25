class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = {}
        
        for r in range(9):
            for c in range(9):
                row_group = r // 3
                col_group = c // 3
                box = (row_group, col_group)
                num = board[r][c]
                if box not in boxes:
                    boxes[box] = set()
                if num == ".":
                    continue
                
                if num in rows[r] or num in cols[c]:
                    return False
                
                if num in boxes[box]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True