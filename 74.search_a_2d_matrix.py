from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i <= j:  # binary search the matrices
            middle = (i + j) // 2
            if (
                matrix[middle][0] <= target and matrix[middle][-1] >= target
            ):  # target possible in matrix row
                array = matrix[middle]
                k = 0
                l = len(array) - 1
                while k <= l:  # binary search
                    middle = (k + l) // 2
                    if array[middle] == target:
                        return True
                    elif array[middle] > target:
                        l = middle - 1
                    elif array[middle] < target:
                        k = middle + 1
                return False
            elif matrix[middle][0] > target:
                j = middle - 1
            elif matrix[middle][0] < target:
                i = middle + 1

        return False  # not found
