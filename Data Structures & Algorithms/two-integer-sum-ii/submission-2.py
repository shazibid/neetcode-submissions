class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         #brute force
         for i in range(0, len(numbers) - 1):
            for j in range(1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        