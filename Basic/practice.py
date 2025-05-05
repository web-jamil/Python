import json

data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Write JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Read JSON data from a file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)  # Output: {'name': 'Alice', 'age': 30, 'is_student': False, 'courses': ['Math', 'Science']}