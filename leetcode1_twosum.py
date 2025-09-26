#attempt from memory for leetcode 1 - twosum 
class Solution(object):
    def twoSum(self, nums, target):
        diffs = dict()
        for i, element in enumerate(nums):
            key = (target - element)
            print(key,element)
            if element in diffs:
                return [diffs[element],i]
            else:
                diffs[key] = i 
