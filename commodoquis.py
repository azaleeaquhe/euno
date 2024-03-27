import json

# Example JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON data into a Python dictionary
data = json.loads(json_data)

# Access the "name" key in the dictionary
name = data["name"]

# Print the value of the "name" key
print(name)  # Output: John
