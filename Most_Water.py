class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        l = 0
        r = len(height) - 1 

        while (l < r):
            width = r - l
            if (height[l] > height[r]):
                maxheight = height[r]
                area = maxheight * width
                r-=1 
            else:
                maxheight = height[l]
                area = maxheight * width
                l+=1 
            
            if (area > max):
                max = area
        
        return max
