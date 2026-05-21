class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        num_set = set(nums)

        longest = 0

        for i in num_set:
            if i-1 not in num_set:
                lenght = 1
                curr = i 
                while curr + 1  in num_set:
                    curr +=1
                    lenght +=1

                longest = max(longest , lenght)
        return longest