from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == '__main__':
    heights = [1, 7, 2, 5, 4, 7, 3, 6]
    print(Solution().maxArea(heights))
