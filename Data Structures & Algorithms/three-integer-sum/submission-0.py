class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        set2 = set()
        nums.sort()

        setter = {}
        for i in range(len(nums)):
            setter[nums[i]] = setter.get(nums[i], 0) + 1

        for i in range(0, len(nums) - 1, 1):
            for j in range(i+1, len(nums), 1):
                third = -(nums[i] + nums[j])
                setter[nums[i]] -= 1
                setter[nums[j]] -= 1

                if setter.get(third, 0) > 0:
                    arr = sorted([nums[i], nums[j], third])
                    set2.add(tuple(arr))
                
                setter[nums[i]] += 1
                setter[nums[j]] += 1
                
        return [list(i) for i in set2]
