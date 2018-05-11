class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    
    def removeElement(self, A, elem):
        i = 0
        for j in range(len(A)):
            if A[j] != elem:
                A[i] = A[j]
                i += 1
        return i