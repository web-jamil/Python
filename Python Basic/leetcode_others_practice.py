def first_negative_integer(arr, k):
    # Result list to store the first negative integer of each window
    result = []
    
    # Queue to store the indices of negative integers
    neg_queue = []
    
    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is negative, add its index to the queue
        if arr[i] < 0:
            neg_queue.append(i)
        
        # Remove elements from the queue that are outside the current window
        if neg_queue and neg_queue[0] < i - k + 1:
            neg_queue.pop(0)
        
        # Add the first negative integer for the current window to the result
        if i >= k - 1:
            if neg_queue:
                result.append(arr[neg_queue[0]])
            else:
                result.append(0)
    
    return result

# Test Cases
if __name__ == "__main__":
    # Example Test Case 1
    arr1 = [-8, 2, 3, -6, 1]
    k1 = 2
    print(first_negative_integer(arr1, k1))  # Output: [-8, 0, -6, -6]

    # Example Test Case 2
    arr2 = [12, -1, -7, 8, -15, 30, 16, 28]
    k2 = 3
    print(first_negative_integer(arr2, k2))  # Output: [-1, -1, -7, -15, -15, 0]

    # Edge Case 1: All Positive Integers
    arr3 = [1, 2, 3, 4, 5]
    k3 = 2
    print(first_negative_integer(arr3, k3))  # Output: [0, 0, 0, 0]

    # Edge Case 2: All Negative Integers
    arr4 = [-1, -2, -3, -4, -5]
    k4 = 3
    print(first_negative_integer(arr4, k4))  # Output: [-1, -2, -3]

    # Edge Case 3: Single Element Windows
    arr5 = [5, -6, 7, -8, 9]
    k5 = 1
    print(first_negative_integer(arr5, k5))  # Output: [0, -6, 0, -8, 0]

    # Edge Case 4: Large Window Size
    arr6 = [-10, 20, -30, 40, -50, 60, -70]
    k6 = 5
    print(first_negative_integer(arr6, k6))  # Output: [-10, -30, -50]
