class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1,len(prices)):
            if prices[i-1]< prices[i]:
                ans+= prices[i]-prices[i-1]
        return ans
