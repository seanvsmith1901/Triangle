class Solution(object):
    # you are an emergency back up option, only to be used if I really need to. thats the whole gist.
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]
