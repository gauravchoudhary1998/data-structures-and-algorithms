class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrow_pos = points[0][1]
        count = 1

        for i in range(1, len(points)):
            if points[i][0] > arrow_pos:        # when do you need a new arrow?
                count += 1
                arrow_pos = points[i][1] # where do you shoot it?

        return count