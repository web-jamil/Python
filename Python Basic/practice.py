# from collections import defaultdict

# class LongestGoodSubarray:
#     def __init__(self, nums, k):
#         """
#         Initialize the object with the input array and the frequency constraint.
#         """
#         self.nums = nums
#         self.k = k

#     def find_longest_good_subarray(self):
#         """
#         Instance method to find the length of the longest good subarray.
#         """
#         freq = defaultdict(int)  # Dictionary to track frequency of elements
#         max_length = 0           # Variable to track the maximum length of a good subarray
#         start = 0                # Sliding window start pointer

#         for end in range(len(self.nums)):
#             # Increment the frequency of the current element
#             freq[self.nums[end]] += 1

#             # If any element's frequency exceeds `k`, shrink the window
#             while freq[self.nums[end]] > self.k:
#                 freq[self.nums[start]] -= 1
#                 if freq[self.nums[start]] == 0:
#                     del freq[self.nums[start]]
#                 start += 1  # Move the window forward

#             # Update the maximum length of a good subarray
#             max_length = max(max_length, end - start + 1)

#         return max_length


# # Test Cases
# if __name__ == "__main__":
#     # Example Test Case 1
#     nums1 = [1, 2, 3, 1, 2, 3, 1, 2]
#     k1 = 2
#     finder1 = LongestGoodSubarray(nums1, k1)
#     print(finder1.find_longest_good_subarray())  # Output: 6

#     # Example Test Case 2
#     nums2 = [1, 2, 1, 2, 1, 2, 1, 2]
#     k2 = 1
#     finder2 = LongestGoodSubarray(nums2, k2)
#     print(finder2.find_longest_good_subarray())  # Output: 2

#     # Example Test Case 3
#     nums3 = [5, 5, 5, 5, 5, 5, 5]
#     k3 = 4
#     finder3 = LongestGoodSubarray(nums3, k3)
#     print(finder3.find_longest_good_subarray())  # Output: 4

#     # Edge Case 1: Single Element Array
#     nums4 = [10]
#     k4 = 1
#     finder4 = LongestGoodSubarray(nums4, k4)
#     print(finder4.find_longest_good_subarray())  # Output: 1

#     # Edge Case 2: No Valid Subarray
#     nums5 = [4, 4, 4, 4]
#     k5 = 0
#     finder5 = LongestGoodSubarray(nums5, k5)
#     print(finder5.find_longest_good_subarray())  # Output: 0

#     # Edge Case 3: Large Array with Uniform Elements
#     nums6 = [7] * 100
#     k6 = 50
#     finder6 = LongestGoodSubarray(nums6, k6)
#     print(finder6.find_longest_good_subarray())  # Output: 50

#     # Edge Case 4: Mixed Array with Large k
#     nums7 = [1, 2, 3, 4, 1, 2, 3, 4, 5]
#     k7 = 3
#     finder7 = LongestGoodSubarray(nums7, k7)
#     print(finder7.find_longest_good_subarray())  # Output: 9

import time 
try:
    print("Starting a long process ....")
    while True:
        print("Working ...")
        time.sleep(1)
except KeyboardInterrupt as e:
    print("An KeyboardInterrupt is happened")
finally:
    print("exiting.... ")