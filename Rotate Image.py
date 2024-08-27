class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix in place (swap along the diagonal)
        # Nice little trick
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[0]) - 1 

            while l<=r:
                temp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = temp
                l+=1
                r-=1
    ''' More memory efficient reflection:
            for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1]= matrix[i][n-j-1], matrix[i][j]
    '''
