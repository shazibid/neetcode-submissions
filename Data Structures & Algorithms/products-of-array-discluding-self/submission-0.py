class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * (len(nums))
        for i in range(1, len(nums), 1):
            #pre
            pre[i] = pre[i-1] * nums[i-1]
        
        #post
        post = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        out = [1] * len(nums)

        for i in range(0, len(nums), 1):
            out[i] = pre[i] * post[i]
        
        return out