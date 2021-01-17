# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t = 0
        b = len(matrix)-1
        l = 0
        r = len(matrix[0])-1
        llist = []
        dir = 0
        while (t<=b and l<=r):
            #print(f"{t} {b} {l} {r}")
            if dir == 0:
                for i in range(l, r+1):
                    llist.append(matrix[t][i])
                    print(matrix[t][i])
                t += 1
            
            elif dir == 1:
                for i in range(t, b+1):
                    llist.append(matrix[i][r])
                    print(matrix[i][r])
                r -= 1
            
            elif dir == 2:
                for i in range(r, l-1, -1):
                    llist.append(matrix[b][i])
                    print(matrix[b][i])
                b-=1
                
            else:
                for i in range(b, t-1, -1):
                    llist.append(matrix[i][l])
                    print(matrix[i][l])
                l+=1
            dir = ((dir+1)%4)
        return llist