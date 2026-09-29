class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        summy = 1
        res = []
        count0 = 0

        for i in nums:
            if i != 0:
                summy = summy * i
            else:
                count0 += 1
        
        if count0 > 1:
            res = [0] * len(nums)

            return res
        
        for i in nums:
            if i != 0 and count0 == 0:
                res.append(summy // i)
            elif i == 0:
                res.append(summy)
            else:
                res.append(0)
        
        return res
