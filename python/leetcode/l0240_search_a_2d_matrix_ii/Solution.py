class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        curRow, curCol = 0, cols - 1

        while curRow < rows and curCol >= 0:
            cur = matrix[curRow][curCol]

            if target < cur:
                curCol -= 1
            elif target > cur:
                curRow += 1
            else:
                return True

        return False
