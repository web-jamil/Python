from collections import deque

class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Calculates the minimum length of a string after repeatedly deleting
        matching prefix and suffix characters.

        This approach uses a deque (double-ended queue) to efficiently
        remove elements from both the front and back of the string.
        The core idea is a greedy strategy: at each step, we remove the
        longest possible prefix and suffix of identical characters.

        Args:
            s: The input string consisting of 'a', 'b', and 'c'.

        Returns:
            The minimum possible length of the string.
        """
        dq = deque(s)
        
        while len(dq) > 1 and dq[0] == dq[-1]:
            ch = dq[0]
            
            # Remove all matching characters from the front
            # This loop runs as long as the deque is not empty and the
            # front character matches 'ch'.
            while dq and dq[0] == ch:
                dq.popleft()
            
            # Remove all matching characters from the back
            # This loop runs as long as the deque is not empty and the
            # back character matches 'ch'.
            while dq and dq[-1] == ch:
                dq.pop()
        
        return len(dq)

# --- Test Cases ---
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Simple deletion
    s1 = "cabaabac"
    expected1 = 0
    result1 = solution.minimumLength(s1)
    print(f"Input: '{s1}', Expected: {expected1}, Result: {result1}, Pass: {result1 == expected1}")
    
    # Test Case 2: Partial deletion with a middle part remaining
    s2 = "aabccabba"
    expected2 = 3
    result2 = solution.minimumLength(s2)
    print(f"Input: '{s2}', Expected: {expected2}, Result: {result2}, Pass: {result2 == expected2}")
    
    # Test Case 3: No deletion possible
    s3 = "ca"
    expected3 = 2
    result3 = solution.minimumLength(s3)
    print(f"Input: '{s3}', Expected: {expected3}, Result: {result3}, Pass: {result3 == expected3}")
    
    # Test Case 4: Single character string (edge case)
    s4 = "a"
    expected4 = 1
    result4 = solution.minimumLength(s4)
    print(f"Input: '{s4}', Expected: {expected4}, Result: {result4}, Pass: {result4 == expected4}")
    
    # Test Case 5: Empty string (edge case, though constraints say 1 <= length)
    s5 = ""
    expected5 = 0
    result5 = solution.minimumLength(s5)
    print(f"Input: '{s5}', Expected: {expected5}, Result: {result5}, Pass: {result5 == expected5}")
    
    # Test Case 6: All characters are the same
    s6 = "bbbbb"
    expected6 = 0
    result6 = solution.minimumLength(s6)
    print(f"Input: '{s6}', Expected: {expected6}, Result: {result6}, Pass: {result6 == expected6}")
    
    # Test Case 7: An alternating string
    s7 = "abacaba"
    expected7 = 1
    result7 = solution.minimumLength(s7)
    print(f"Input: '{s7}', Expected: {expected7}, Result: {result7}, Pass: {result7 == expected7}")