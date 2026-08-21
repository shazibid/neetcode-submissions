import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        #method: store the new values, sort them, return values at the indx of length - k
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]
