class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i , j= 0 , len(heights) - 1
        marea = -999

        while i < j:
            width = j - i
            area = width * min(heights[i], heights[j])
            marea = max(marea , area)

            if heights[j] >= heights[i]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
        return marea