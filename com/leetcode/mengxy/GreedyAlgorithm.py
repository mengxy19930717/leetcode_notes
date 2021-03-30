from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        res = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                res += 1
            else:
                end = intervals[i][1]
        return res


    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 1:
            return 0
        points.sort(key=lambda x: (x[1], x[0]))
        res = 0
        end = points[0][1]
        for i in range(1, len(points)):
            if end >= points[i][0]:
                res += 1
            else:
                end = points[i][1]
        return len(points) - res


    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])
        for i in range(1, len(people)):
            tmp = people.pop(i)
            people.insert(tmp[1], tmp)
        return people


    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > min_value:
                max_profit = max(prices[i] - min_value, max_profit)
            else:
                min_value = prices[i]
        return max_profit


    


if __name__ == '__main__':
    so = Solution()
    print(so.reconstructQueue(people=[[9,0],[7,0],[1,9],[3,0],[2 ,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
    print(so.maxProfit(prices=[7,1,5,3,4,6]))


