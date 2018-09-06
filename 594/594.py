class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        maximum = 0
        for item in nums:
            if item not in numDict:
                numDict[item] = 1
            else:
                numDict[item] += 1

        for key, value in numDict.items():
            if key + 1 in numDict:
                num = numDict[key] + numDict[key+1]
                if num > maximum:
                    maximum = num

        return maximum
