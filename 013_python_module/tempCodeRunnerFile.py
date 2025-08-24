class Solution:
    def divisibleAndNonDivisibleSumsDifference(self, n: int, m: int) -> int:
        num1 = 0  # Sum of integers not divisible by m
        num2 = 0  # Sum of integers divisible by m

        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        return num1 - num2

print("Test Cases:")
sol = Solution()
print(f"n=10, m=3 -> {sol.divisibleAndNonDivisibleSumsDifference(10, 3)}") # Expected: 19
print(f"n=5, m=6 -> {sol.divisibleAndNonDivisibleSumsDifference(5, 6)}")   # Expected: 15
print(f"n=5, m=1 -> {sol.divisibleAndNonDivisibleSumsDifference(5, 1)}")   # Expected: -15