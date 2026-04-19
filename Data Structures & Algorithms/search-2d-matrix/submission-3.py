class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        n = len(matrix)
        m = len(matrix[0])
        if not matrix or not matrix[0]:
            return False
        
        end = (m) * (n) - 1
        while end >= start and end >= 0:
            mid = (end + start)//2
            i = mid//m
            j = mid%m
            print(f"{start} {mid} {end}")
            print(matrix[i][j])
            if matrix[i][j] > target:
                end = mid - 1
            elif matrix[i][j] < target:
                start = mid + 1
            else:
                return True

        return False;