class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        C = A[:]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if C[i] < B[j]:
                A[k] = C[i]
                i += 1
            else:
                A[k] = B[j]
                j += 1
            k += 1
        while i < m:
            A[k] = C[i]
            i += 1
            k += 1
        while j < n:
            A[k] = B[j]
            j += 1
            k += 1