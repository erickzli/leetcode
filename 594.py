class Solution:
    '''
    We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
    Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

    Example 1:
    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].
    Note: The length of the input array will not exceed 20,000.
    '''
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
