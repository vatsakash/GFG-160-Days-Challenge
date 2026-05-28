class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        sorted_arr = sorted(arr)
        greatest_element = sorted_arr[-1]
        for i in range(n-2,-1,-1):
            if sorted_arr[i] != greatest_element:
                return sorted_arr[i]
        return -1
    
obj = Solution()
obj.getSecondLargest([12, 35, 1, 10, 34, 1])