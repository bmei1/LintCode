# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        res = 0
        for i in range(len(points)):
            slope = {'inf' : 0}
            samep = 1
            for j in range(len(points)):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[j].y - points[i].y)/(points[j].x - points[i].x)
                    if k in slope:
                        slope[k] += 1
                    else:
                        slope[k] = 1
                else:
                    samep += 1
            res = max(res, max(slope.values()) + samep)
        return res