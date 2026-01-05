class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        n = len(heights)
        while stack:
            idx, height = stack.pop()
            max_area = max(max_area, height * (n - idx))

        return max_area
