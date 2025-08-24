# --- Set Theory Applications in Python (Code Examples) ---

# -------------------- 1. Finding Common Interests --------------------

# Imagine two groups of people and their hobbies
group_a_hobbies = {"reading", "hiking", "coding", "photography"}
group_b_hobbies = {"coding", "gaming", "photography", "traveling"}

# Finding common hobbies (intersection)
common_hobbies = group_a_hobbies & group_b_hobbies
print(f"Common hobbies: {common_hobbies}")

# Finding hobbies unique to each group (difference)
hobbies_only_in_a = group_a_hobbies - group_b_hobbies
print(f"Hobbies only in Group A: {hobbies_only_in_a}")

hobbies_only_in_b = group_b_hobbies - group_a_hobbies
print(f"Hobbies only in Group B: {hobbies_only_in_b}")

# Finding all unique hobbies across both groups (union)
all_hobbies = group_a_hobbies | group_b_hobbies
print(f"All unique hobbies: {all_hobbies}")

# Finding hobbies that are in one group or the other, but not both (symmetric difference)
unique_to_either = group_a_hobbies ^ group_b_hobbies
print(f"Hobbies unique to either group: {unique_to_either}")

# -------------------- 2. Filtering Unique Items --------------------

# Removing duplicate entries from a list
data_with_duplicates = [1, 5, 2, 5, 3, 1, 4, 2, 2]
unique_data = set(data_with_duplicates)
print(f"Unique data: {unique_data}")

# Identifying unique words in a sentence (case-insensitive)
sentence = "The quick brown fox jumps over the lazy quick dog."
words = sentence.lower().split()
unique_words = set(words)
print(f"Unique words in the sentence: {unique_words}")

# -------------------- 3. Checking for Subsets and Supersets (Permissions/Access Control) --------------------

admin_permissions = {"read", "write", "delete", "execute"}
user_permissions_1 = {"read", "write"}
user_permissions_2 = {"read", "execute", "modify"}

# Checking if user_permissions_1 is a subset of admin_permissions
can_user1_do_all_admin_tasks = user_permissions_1.issubset(admin_permissions)
print(f"Can user 1 do all admin tasks? {can_user1_do_all_admin_tasks}")

# Checking if admin_permissions is a superset of user_permissions_2
does_admin_have_all_user2_permissions = admin_permissions.issuperset(user_permissions_2)
print(f"Does admin have all user 2 permissions? {does_admin_have_all_user2_permissions}")

# -------------------- 4. Database Operations (Simplified) --------------------

# Imagine two sets of user IDs from different database tables
active_users = {101, 102, 103, 104, 105}
users_with_purchases = {103, 105, 106, 107}

# Finding users who are active AND have made purchases (intersection - JOIN)
active_buyers = active_users & users_with_purchases
print(f"Active users who made purchases: {active_buyers}")

# Finding all unique users (union - UNION)
all_users = active_users | users_with_purchases
print(f"All unique users: {all_users}")

# Finding active users who have NOT made purchases (difference - LEFT JOIN WHERE purchase IS NULL)
active_non_buyers = active_users - users_with_purchases
print(f"Active users who haven't made purchases: {active_non_buyers}")

# -------------------- 5. Network Analysis (Basic) --------------------

# Representing connections between nodes in a network
node_a_connections = {"node_b", "node_c", "node_d"}
node_c_connections = {"node_a", "node_e", "node_f"}

# Finding common connections between node A and node C
common_connections = node_a_connections & node_c_connections
print(f"Common connections between Node A and Node C: {common_connections}")

# Finding all unique nodes connected to either A or C
all_connected_nodes = node_a_connections | node_c_connections
print(f"All nodes connected to A or C: {all_connected_nodes}")

# -------------------- 6. Recommendation Systems (Simple) --------------------

# User preferences for movies
user_a_likes = {"action", "sci-fi", "thriller"}
user_b_likes = {"comedy", "romance", "sci-fi"}
user_c_likes = {"action", "drama", "thriller"}

# Finding movies liked by both User A and User C
common_likes_ac = user_a_likes & user_c_likes
print(f"Movies liked by both User A and User C: {common_likes_ac}")

# Suggesting movies to User B based on User A's preferences (if some overlap exists)
if "sci-fi" in user_a_likes & user_b_likes:
    suggestions_for_b = user_a_likes - user_b_likes
    print(f"Potential movie suggestions for User B based on User A: {suggestions_for_b}")
else:
    print("No common liked genres between User A and User B to make direct suggestions.")

# -------------------- 7. Data Cleaning and Preprocessing --------------------

# Identifying and removing outliers (simplified example)
all_data_points = {10, 12, 15, 11, 18, 100, 9, 13, 105}
normal_range = set(range(8, 20))  # Define a "normal" range

outliers = all_data_points - normal_range
print(f"Potential outliers: {outliers}")

inliers = all_data_points & normal_range
print(f"Data points within the normal range: {inliers}")

# -------------------- Summary of Applications --------------------
# Set theory provides powerful tools for:
# - Comparing and contrasting groups of data.
# - Identifying unique elements.
# - Managing permissions and access control.
# - Performing basic database-like operations.
# - Analyzing relationships in networks.
# - Building simple recommendation systems.
# - Cleaning and preprocessing data by identifying unique or overlapping elements.