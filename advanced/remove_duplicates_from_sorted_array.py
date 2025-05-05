""" Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order. """



""" ### **Problem Explanation**

Given a sorted integer array `nums`, we need to **remove duplicates in-place** such that each unique element appears only once. The relative order of the elements should be maintained. After removing duplicates, we should return the number of unique elements (`k`). The first `k` elements of the array should contain the unique elements, and the remaining elements can be ignored.

#### **Key Points:**
1. **In-Place Modification:**
   - The array `nums` should be modified in-place without using extra space for another array.

2. **Relative Order:**
   - The order of the unique elements should remain the same as in the original array.

3. **Return Value:**
   - The function should return the number of unique elements (`k`).

---

### **Approach: Two-Pointer Technique**

We can solve this problem efficiently using the **Two-Pointer Technique**. Here's how it works:

1. **Initialize Two Pointers:**
   - `left`: Tracks the position where the next unique element should be placed.
   - `right`: Iterates through the array to find unique elements.

2. **Iterate Through the Array:**
   - If `nums[right]` is not equal to `nums[left]`, it means we have found a new unique element.
   - Move `left` forward and place the new unique element at `nums[left]`.

3. **Return the Number of Unique Elements:**
   - The value of `left + 1` gives the number of unique elements.

#### **Time Complexity:** \(O(n)\), where \(n\) is the length of the array.
- We traverse the array once.

#### **Space Complexity:** \(O(1)\).
- We use constant extra space.

---

### **Python Implementation**

```python
def removeDuplicates(nums):
    if not nums:
        return 0

    left = 0  # Pointer to track the position of the last unique element

    for right in range(1, len(nums)):
        # If the current element is not equal to the last unique element
        if nums[right] != nums[left]:
            left += 1  # Move the left pointer
            nums[left] = nums[right]  # Place the new unique element

    # The number of unique elements is left + 1
    return left + 1

# Test cases
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2 [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5 [0, 1, 2, 3, 4]
```

---

### **Step-by-Step Explanation**

#### **Example 1: `nums = [1, 1, 2]`**

1. **Initialization:**
   - `left = 0`, `nums = [1, 1, 2]`.

2. **Iteration:**
   - `right = 1`, `nums[right] = 1`:
     - `nums[right] == nums[left]` (both are `1`), so do nothing.
   - `right = 2`, `nums[right] = 2`:
     - `nums[right] != nums[left]` (`2 != 1`), so:
       - Move `left` to `1`.
       - Place `nums[right]` at `nums[left]`: `nums = [1, 2, 2]`.

3. **Result:**
   - The number of unique elements is `left + 1 = 2`.
   - The modified array is `[1, 2, _]`.

---

#### **Example 2: `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`**

1. **Initialization:**
   - `left = 0`, `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`.

2. **Iteration:**
   - `right = 1`, `nums[right] = 0`:
     - `nums[right] == nums[left]` (both are `0`), so do nothing.
   - `right = 2`, `nums[right] = 1`:
     - `nums[right] != nums[left]` (`1 != 0`), so:
       - Move `left` to `1`.
       - Place `nums[right]` at `nums[left]`: `nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]`.
   - `right = 3`, `nums[right] = 1`:
     - `nums[right] == nums[left]` (both are `1`), so do nothing.
   - `right = 4`, `nums[right] = 1`:
     - `nums[right] == nums[left]` (both are `1`), so do nothing.
   - `right = 5`, `nums[right] = 2`:
     - `nums[right] != nums[left]` (`2 != 1`), so:
       - Move `left` to `2`.
       - Place `nums[right]` at `nums[left]`: `nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]`.
   - `right = 6`, `nums[right] = 2`:
     - `nums[right] == nums[left]` (both are `2`), so do nothing.
   - `right = 7`, `nums[right] = 3`:
     - `nums[right] != nums[left]` (`3 != 2`), so:
       - Move `left` to `3`.
       - Place `nums[right]` at `nums[left]`: `nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]`.
   - `right = 8`, `nums[right] = 3`:
     - `nums[right] == nums[left]` (both are `3`), so do nothing.
   - `right = 9`, `nums[right] = 4`:
     - `nums[right] != nums[left]` (`4 != 3`), so:
       - Move `left` to `4`.
       - Place `nums[right]` at `nums[left]`: `nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]`.

3. **Result:**
   - The number of unique elements is `left + 1 = 5`.
   - The modified array is `[0, 1, 2, 3, 4, _, _, _, _, _]`.

---

### **Edge Cases**

1. **Empty Array:**
   - Input: `[]`
   - Output: `0`, `[]`

2. **Single Element:**
   - Input: `[5]`
   - Output: `1`, `[5]`

3. **All Elements the Same:**
   - Input: `[2, 2, 2]`
   - Output: `1`, `[2]`

4. **No Duplicates:**
   - Input: `[1, 2, 3, 4]`
   - Output: `4`, `[1, 2, 3, 4]`

---

### **Testing the Function**

```python
# Test cases
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2 [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 5 [0, 1, 2, 3, 4]

nums3 = []
k3 = removeDuplicates(nums3)
print(k3, nums3[:k3])  # Output: 0 []

nums4 = [5]
k4 = removeDuplicates(nums4)
print(k4, nums4[:k4])  # Output: 1 [5]

nums5 = [2, 2, 2]
k5 = removeDuplicates(nums5)
print(k5, nums5[:k5])  # Output: 1 [2]

nums6 = [1, 2, 3, 4]
k6 = removeDuplicates(nums6)
print(k6, nums6[:k6])  # Output: 4 [1, 2, 3, 4]
```

---

### **Time and Space Complexity**

1. **Time Complexity:** \(O(n)\), where \(n\) is the length of the array.
   - We traverse the array once.

2. **Space Complexity:** \(O(1)\).
   - We use constant extra space.

---

This approach is efficient and easy to understand. Let me know if you need further clarification! """