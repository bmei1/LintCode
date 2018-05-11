class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        l = 0
        r = len(A) - 1
        while l <= r:
            m = (l + r) // 2
            if A[m] == target:
                return m
            if A[m] >= A[l]:
                if A[m] > target and target >= A[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif A[m] < A[r]:
                if A[m] < target and target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1