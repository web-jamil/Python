def num_equivalent_domino_pairs_optimized_hash_map(dominoes):
    counts = {}
    
    # Normalize representation and count occurrences
    for d in dominoes:
        a, b = sorted(d)  # Ensuring the smaller number comes first
        key = a * 10 + b  # Unique identifier for the pair
        counts[key] = counts.get(key, 0) + 1

    # Compute pairs using combinatorial formula
    ans = sum(count * (count - 1) // 2 for count in counts.values())

    return ans

# **Test Cases**
test_cases = [
    ([[1,2],[2,1],[3,4],[5,6]], 1),  # Basic case with one equivalent pair
    ([[1,2],[1,2],[1,1],[1,2],[2,2]], 3),  # Multiple repeating pairs
    ([[1,1],[1,1],[2,2],[2,2]], 4),  # Fully paired dominoes
    ([[1,2],[3,4],[5,6]], 0),  # No pairs
    ([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]], 0),  # All distinct pairs
    ([[1,9],[9,1],[2,8],[8,2],[3,7],[7,3]], 3),  # Edge case with larger values
]

# **Run Tests**
for i, (dominoes, expected) in enumerate(test_cases):
    result = num_equivalent_domino_pairs_optimized_hash_map(dominoes)
    print(f"Test {i+1}: {'Pass' if result == expected else 'Fail'} (Output: {result}, Expected: {expected})")
