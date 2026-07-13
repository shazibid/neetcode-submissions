class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #im so irritated

        arr = []
        zero_cnt = 0
        prod = 1

        for i in nums:
            if i == 0:
                zero_cnt += 1
                if zero_cnt > 1:
                    arr = [0]*len(nums)
                    return arr
            else:
                prod *= i
        
        for i in nums:
            if i == 0:
                arr.append(prod)
            elif zero_cnt > 0:
                arr.append(0)
            else:
                arr.append(prod // i)

        return arr


