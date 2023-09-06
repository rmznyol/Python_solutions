#435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end_point = intervals[0][1]
        count = 0
        for interval in intervals[1:]:
            if interval[0] < end_point: #intersects
                end_point = min(interval[1],end_point)
                count += 1
            else:
                end_point = interval[1]
        return count
##########################################
# 452. Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        end_point = points[0][1]
        count = 0
        for point in points[1:]:
            if point[0] <= end_point: #intersects
                end_point = min(point[1],end_point)
                count += 1
            else:
                end_point = point[1]
        return len(points) - count
