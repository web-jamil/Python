# --- Applications of Sets in Python (Code Examples - Revisited for Clarity) ---

# -------------------- 1. Deduplication of Data --------------------

# Scenario: You have a list of items with duplicates and need to get only the unique items.

data_with_duplicates = [1, 5, 2, 5, 3, 1, 4, 2, 2]

# Using a set to efficiently remove duplicates
unique_data = set(data_with_duplicates)
print(f"Original data: {data_with_duplicates}")
print(f"Unique data (using set): {unique_data}")

# Another example: Unique words in a text file
text = """This is a sample text with some repeated words.
This text has the word text repeated."""
words = text.lower().split()
unique_words = set(words)
print(f"\nOriginal words: {words}")
print(f"Unique words: {unique_words}")

# -------------------- 2. Membership Testing --------------------

# Scenario: You need to quickly check if an element exists in a collection. Sets are highly efficient for this.

allowed_users = {"alice", "bob", "charlie"}
user_to_check = "bob"

if user_to_check in allowed_users:
    print(f"\nUser '{user_to_check}' is allowed.")
else:
    print(f"\nUser '{user_to_check}' is not allowed.")

# Comparing performance with lists (for large datasets, sets are much faster)
large_list = list(range(1_000_000))
large_set = set(range(1_000_000))
number_to_find = 999_999

import time

start_time = time.time()
is_in_list = number_to_find in large_list
end_time = time.time()
print(f"\nTime to check in list: {end_time - start_time:.6f} seconds")

start_time = time.time()
is_in_set = number_to_find in large_set
end_time = time.time()
print(f"Time to check in set: {end_time - start_time:.6f} seconds")

# -------------------- 3. Set Operations for Data Analysis --------------------

# Scenario: Comparing two groups of data to find similarities and differences.

group_a = {"apple", "banana", "cherry", "date"}
group_b = {"banana", "date", "fig", "grape"}

# Intersection: Elements present in both groups
common_items = group_a & group_b
print(f"\nCommon items: {common_items}")

# Union: All unique elements from both groups
all_items = group_a | group_b
print(f"All unique items: {all_items}")

# Difference (A - B): Elements in group A but not in group B
only_in_a = group_a - group_b
print(f"Items only in Group A: {only_in_a}")

# Difference (B - A): Elements in group B but not in group A
only_in_b = group_b - group_a
print(f"Items only in Group B: {only_in_b}")

# Symmetric Difference: Elements present in either group A or B, but not both
unique_to_either = group_a ^ group_b
print(f"Items unique to either group: {unique_to_either}")

# -------------------- 4. Relationship Analysis (Subsets and Supersets) --------------------

# Scenario: Checking if one set of items is contained within another (e.g., permissions).

all_permissions = {"read", "write", "delete", "execute"}
user_permissions = {"read", "write"}
admin_permissions = {"read", "write", "delete", "execute", "manage_users"}

# Checking if user_permissions are a subset of all_permissions
can_user_do_basic = user_permissions.issubset(all_permissions)
print(f"\nCan user do basic operations? {can_user_do_basic}")

# Checking if admin_permissions are a superset of all_permissions
does_admin_have_all_basic = admin_permissions.issuperset(all_permissions)
print(f"Does admin have all basic permissions? {does_admin_have_all_basic}")

# -------------------- 5. Filtering Based on Set Membership --------------------

# Scenario: You have a list of items and want to filter out those that belong to a specific set.

all_products = ["apple", "banana", "orange", "grape", "melon", "kiwi"]
forbidden_fruits = {"banana", "melon"}

allowed_products = [product for product in all_products if product not in forbidden_fruits]
print(f"\nAll products: {all_products}")
print(f"Forbidden fruits: {forbidden_fruits}")
print(f"Allowed products: {allowed_products}")

# -------------------- 6. Efficiently Tracking Unique Occurrences --------------------

# Scenario: Counting the number of unique events in a log.

log_entries = ["login", "logout", "login", "error", "login", "success", "error"]
unique_events = set(log_entries)
number_of_unique_events = len(unique_events)
print(f"\nLog entries: {log_entries}")
print(f"Unique events: {unique_events}")
print(f"Number of unique events: {number_of_unique_events}")

# -------------------- 7. Building Simple Search Functionality --------------------

# Scenario: Checking if any keywords from a query exist in a set of indexed terms.

indexed_terms = {"python", "programming", "sets", "data", "structures", "algorithms"}
search_query = "learn about python data structures"
query_keywords = set(search_query.lower().split())

relevant_keywords = query_keywords & indexed_terms
if relevant_keywords:
    print(f"\nSearch query: '{search_query}'")
    print(f"Relevant keywords found: {relevant_keywords}")
else:
    print(f"\nNo relevant keywords found for query: '{search_query}'")

# -------------------- 8. Representing Relationships (Graph Nodes) --------------------

# Scenario: Representing the neighbors of a node in a graph.

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'}
}

node = 'B'
neighbors = graph.get(node, set())
print(f"\nNeighbors of node '{node}': {neighbors}")

# Finding common neighbors between two nodes
node1 = 'A'
node2 = 'C'
neighbors1 = graph.get(node1, set())
neighbors2 = graph.get(node2, set())
common_neighbors = neighbors1 & neighbors2
print(f"Common neighbors of '{node1}' and '{node2}': {common_neighbors}")

# In summary, sets are a fundamental data structure in Python with numerous applications due to their ability to store unique elements and perform efficient set theory operations and membership testing. They are valuable in various domains like data analysis, algorithm design, and general programming tasks involving collections of items.