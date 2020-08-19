class Solution:
    def maxSubArray(self, num):

        if len(num) == 1:
            return num[0]

        sum_result = [0 for i in range(len(num))]
        sum_result[0] = num[0]

        for i in range(1, len(num)):
            if sum_result[i - 1] < 0:
                sum_result[i] = num[i]
            else:
                sum_result[i] = sum_result[i - 1] + num[i]
        return max(sum_result)
a=Solution()

a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])