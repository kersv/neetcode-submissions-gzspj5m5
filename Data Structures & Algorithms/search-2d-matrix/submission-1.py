class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get height and width to get totalElements of matrix 
        height = len(matrix)
        width = len(matrix[0])
        # low and high for 2 pointers indexes, low = 0, high = (m*n) -1 
        low, high = 0, (height * width)-1
        # treat like a 1d Array and split it in the middle 
        while low <= high:
            # middle(index) = totalElements // 2
            middle = (low + high) // 2
            
            # get value at middle by getting row and col
            # row = middle // (number of columns aka width of a row)
            # col = middle % (number of columns, to get remainder)
            row = middle // width
            col = middle % width
            # check if matrix[row][col] equal to target, return True
            if matrix[row][col] == target:
                return True
            # elif matrix[row][col] < target, look rightside
            elif matrix[row][col] < target:
                low = middle +1
            # else look leftside
            else:
                high = middle -1
        return False



