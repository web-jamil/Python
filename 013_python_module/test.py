from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        min_deletions = float('inf')

        for base in set(freq.values()):
            deletions = 0
            for f in freq.values():
                if f < base:
                    deletions += f
                elif f > base + k:
                    deletions += f - (base + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
sol = Solution()

# Provided examples
print(sol.minimumDeletions("aabcaba", 0))        # ➤ 3
print(sol.minimumDeletions("dabdcbdcdcd", 2))    # ➤ 2
print(sol.minimumDeletions("aaabaaa", 2))        # ➤ 1

# Edge cases
print(sol.minimumDeletions("a", 0))              # ➤ 0 (Single character)
print(sol.minimumDeletions("abc", 2))            # ➤ 0 (All frequencies 1, diff ≤ k)
print(sol.minimumDeletions("aaaaa", 0))          # ➤ 0 (Uniform frequency)
print(sol.minimumDeletions("aabbcc", 0))         # ➤ 0 (All frequencies equal)
print(sol.minimumDeletions("aabbcc", 1))         # ➤ 0 (Still within k)
print(sol.minimumDeletions("aabbccc", 0))        # ➤ 1 (Need to delete one 'c')
print(sol.minimumDeletions("zzxyyx", 0))         # ➤ 2 (Make all frequencies equal)
print(sol.minimumDeletions("abcabcabcabc", 0))   # ➤ 0 (Perfectly balanced)
print(sol.minimumDeletions("abcabcabcabc", 1))   # ➤ 0 (Still balanced within k)