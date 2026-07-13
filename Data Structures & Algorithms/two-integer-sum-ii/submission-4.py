class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         #brute force
         l = 0
         r = len(numbers) - 1

         while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            
            elif target > total: ####
                l += 1
            else:
                r -= 1

        