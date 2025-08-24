import pandas as pd
import numpy as np

print("--- Logic in Python and Pandas Practice Code ---")

# --- 1. Python Logic Basics ---
print("\n--- 1. Python Logic Basics ---")

# 1.1 Conditional Statements (if-elif-else)
score = 85
if score >= 90:
    print(f"{score}: Excellent!")
elif score >= 70:
    print(f"{score}: Good job!")
else:
    print(f"{score}: Keep practicing.")

temperature = 28 # degrees Celsius
if temperature > 30:
    print("It's a hot day!")
elif 20 <= temperature <= 30:
    print("It's a pleasant day.")
else:
    print("It's a bit chilly.")

# 1.2 Comparison Operators
a = 10
b = 20
print(f"\n{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} >= {b}: {a >= b}")

# 1.3 Logical Operators (and, or, not)
is_student = True
has_discount = False
age = 22

# Using 'and'
if is_student and age >= 18:
    print("\nEligible for student discount.")
else:
    print("\nNot eligible for student discount (must be student and adult).")

# Using 'or'
if has_discount or is_student:
    print("User qualifies for some form of special offer.")
else:
    print("No special offers apply.")

# Using 'not'
is_active = False
if not is_active:
    print("User account is inactive.")

# Combining operators
if (age > 20 and is_student) or has_discount:
    print("Complex condition met.")
else:
    print("Complex condition not met.")

# 1.4 Truthiness (non-empty, non-zero values are True)
my_list = [1, 2]
my_string = "hello"
my_number = 5
empty_list = []
zero_number = 0

if my_list:
    print("\nList is not empty (truthy).")
if my_string:
    print("String is not empty (truthy).")
if my_number:
    print("Number is non-zero (truthy).")
if not empty_list:
    print("Empty list is falsy.")
if not zero_number:
    print("Zero number is falsy.")

# 1.5 Loops with Logic
numbers = [1, 5, 8, 12, 3, 9, 20]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(f"\nEven numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")


print("\n--- 2. Pandas Logic: Vectorized Operations and Filtering ---")

# --- Setup: Create a Sample DataFrame ---
data = {
    'TransactionID': np.arange(101, 121),
    'CustomerID': np.random.randint(1001, 1005, 20),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Speakers'], 20),
    'Category': np.random.choice(['Electronics', 'Peripherals', 'Accessories'], 20),
    'Amount_USD': np.random.uniform(10, 1500, 20).round(2),
    'Quantity': np.random.randint(1, 5, 20),
    'IsMember': np.random.choice([True, False], 20),
    'Rating': np.random.randint(1, 6, 20), # 1 to 5 stars
    'OrderDate': pd.to_datetime(pd.date_range(start='2024-01-01', periods=20, freq='D')),
    'ShippingStatus': np.random.choice(['Pending', 'Shipped', 'Delivered', np.nan], 20, p=[0.2, 0.3, 0.4, 0.1]),
    'Notes': ['Urgent', 'Standard', 'Fragile', np.nan] * 5 # Mix of strings and NaNs
}
df = pd.DataFrame(data)

# Introduce some more NaNs for `isna()` demos
df.loc[[3, 7, 12], 'Amount_USD'] = np.nan
df.loc[[1, 8, 11], 'Rating'] = np.nan

print("\nOriginal DataFrame (df.head()):\n", df.head())
print("\nDataFrame Info:\n")
df.info()


# 2.1 Boolean Indexing / Masking (Fundamental Pandas Logic)
# Select rows where 'Amount_USD' is greater than 500
high_value_transactions = df[df['Amount_USD'] > 500]
print("\nTransactions with Amount_USD > 500:\n", high_value_transactions)

# Select rows where 'Category' is 'Electronics'
electronics_orders = df[df['Category'] == 'Electronics']
print("\nOrders in 'Electronics' category:\n", electronics_orders.head())

# Select rows where 'IsMember' is True
member_transactions = df[df['IsMember']] # No need for == True
print("\nTransactions by Members:\n", member_transactions.head())

# 2.2 Multiple Conditions (AND: &, OR: |, NOT: ~)
# Orders in 'Electronics' category AND Amount_USD > 1000
electronics_expensive_orders = df[(df['Category'] == 'Electronics') & (df['Amount_USD'] > 1000)]
print("\nElectronics orders > 1000 USD:\n", electronics_expensive_orders)

# Orders in 'Books' OR 'Accessories' category
books_or_accessories = df[(df['Category'] == 'Books') | (df['Category'] == 'Accessories')]
print("\nOrders in 'Books' OR 'Accessories' category:\n", books_or_accessories.head())

# Orders NOT by CustomerID 1001
not_customer_1001 = df[~(df['CustomerID'] == 1001)]
print("\nOrders NOT by CustomerID 1001:\n", not_customer_1001.head())

# Complex combination: (High Amount OR High Quantity) AND IsMember
complex_filter = df[((df['Amount_USD'] > 700) | (df['Quantity'] >= 3)) & (df['IsMember'])]
print("\nComplex filter: (Amount > 700 OR Quantity >= 3) AND IsMember:\n", complex_filter)

# 2.3 Using .isin() for multiple discrete values
# Products that are 'Laptop' or 'Monitor' or 'Keyboard'
specific_products = df[df['Product'].isin(['Laptop', 'Monitor', 'Keyboard'])]
print("\nOrders for Laptop, Monitor, or Keyboard (using .isin()):\n", specific_products)

# 2.4 Using .between() for numerical ranges
# Amounts between 100 and 500 (inclusive)
medium_range_amounts = df[df['Amount_USD'].between(100, 500)]
print("\nOrders with Amount_USD between 100 and 500:\n", medium_range_amounts.head())

# 2.5 String Methods with Logic (`.str.`)
# Products whose names contain 'Mouse'
mouse_related_products = df[df['Product'].str.contains('Mouse', na=False)] # na=False handles NaNs
print("\nProducts containing 'Mouse':\n", mouse_related_products)

# Categories that start with 'Elec'
elec_categories = df[df['Category'].str.startswith('Elec', na=False)]
print("\nCategories starting with 'Elec':\n", elec_categories.head())

# 2.6 Missing Data Logic (`.isna()`, `.notna()`)
# Transactions with missing ShippingStatus
missing_shipping_status = df[df['ShippingStatus'].isna()]
print("\nTransactions with missing ShippingStatus:\n", missing_shipping_status)

# Transactions with a non-missing Rating
rated_transactions = df[df['Rating'].notna()]
print("\nTransactions with a valid Rating:\n", rated_transactions.head())

# 2.7 Conditional Column Creation / Modification (`np.where`, `assign`)
# Create a 'Discount_Eligibility' column
df['Discount_Eligibility'] = np.where(df['Amount_USD'] > 700, 'High_Value_Customer', 'Standard_Customer')
print("\nDataFrame with 'Discount_Eligibility' column:\n", df[['Amount_USD', 'Discount_Eligibility']].head())

# Create a 'Tier' based on CustomerID (multiple conditions using np.select)
conditions = [
    df['CustomerID'] == 1001,
    df['CustomerID'] == 1002,
    df['CustomerID'] == 1003
]
choices = ['Gold', 'Silver', 'Bronze']
df['CustomerTier'] = np.select(conditions, choices, default='New') # 'New' for other CustomerIDs
print("\nDataFrame with 'CustomerTier' based on CustomerID:\n", df[['CustomerID', 'CustomerTier']].head())

# Update Quantity: If Category is 'Accessories', increase Quantity by 1
df['Adjusted_Quantity'] = df.apply(lambda row: row['Quantity'] + 1 if row['Category'] == 'Accessories' else row['Quantity'], axis=1)
print("\nDataFrame with 'Adjusted_Quantity' (for Accessories):\n", df[['Category', 'Quantity', 'Adjusted_Quantity']].head())

# 2.8 Conditional Replacement (`.where()`, `.mask()`)
# .where(condition, other=value): Replaces values where condition is FALSE
df_where = df.copy()
df_where['Rating_Adjusted'] = df_where['Rating'].where(df_where['Rating'] >= 3, 0) # Ratings < 3 become 0
print("\nDataFrame with 'Rating_Adjusted' (Ratings < 3 set to 0):\n", df_where[['Rating', 'Rating_Adjusted']].head())

# .mask(condition, other=value): Replaces values where condition is TRUE
df_mask = df.copy()
df_mask['Amount_Masked'] = df_mask['Amount_USD'].mask(df_mask['Amount_USD'] < 50, np.nan) # Amounts < 50 become NaN
print("\nDataFrame with 'Amount_Masked' (Amounts < 50 set to NaN):\n", df_mask[['Amount_USD', 'Amount_Masked']].head())

# 2.9 Using .query() for Filtering (String-based Logic)
# (Covered in more detail in a separate request, but essential for logic)
query_result = df.query('Category == "Electronics" and Amount_USD > 500')
print("\nOrders filtered by .query() (Category 'Electronics' AND Amount_USD > 500):\n", query_result.head())

# Using external variables with @ in query
min_rating = 4
member_status = True
query_external_vars = df.query('Rating >= @min_rating and IsMember == @member_status')
print(f"\nOrders filtered by .query() (Rating >= {min_rating} AND IsMember is {member_status}):\n", query_external_vars.head())


print("\n--- End of Logic in Python and Pandas Code ---")