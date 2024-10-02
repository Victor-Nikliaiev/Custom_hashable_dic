# Custom Hashable Dictionary (`HashableDic`)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description

This repository contains a custom Python class `HashableDic` that implements a hashable dictionary. This dictionary can be used as a key in other dictionaries, an element in sets, or any other context where hashability is required. It allows for adding, removing, and accessing items while maintaining hashability, even when the dictionary is modified.

## Features

-   **Hashable Dictionary**: The `HashableDic` class ensures that the dictionary is hashable and can be used in hashable contexts like keys in dictionaries or elements in sets.
-   **Mutable Yet Hashable**: The class tracks changes to the dictionary and recalculates its hash only when necessary, ensuring efficient hash management.
-   **Dictionary Additions**: You can add individual key-value pairs or another dictionary, with checks to ensure structural compatibility.
-   **Custom Item Hashing**: The class converts nested dictionaries into hashable objects automatically.

## Installation

To use the `HashableDic` class, simply clone this repository or copy the class code from `hashable_dic.py` into your Python project.

```bash
git clone https://github.com/Victor-Nikliaiev/Custom_hashable_dic.git
```

Then, import and use the `HashableDic` class in your Python code:

```python
from hashable_dic import HashableDic

# Example usage
my_dict = HashableDic({'a': 1, 'b': 2})
print(hash(my_dict))  # Outputs the hash of the dictionary
```

## Usage

### Example 1: Creating and Adding Items

```python
print("-" * 100)
fruits = HashableDic({
    "apple": 1,
    "orange": 2,
    "banana": 3
})

# Adding a new dictionary
fruits.add({
    "mango": 4,
    "pineapple": 5})

# Adding a single key-value pair
fruits.add("grape", 6)

print(fruits)  # Output: {'apple': 1, 'orange': 2, 'banana': 3, 'mango': 4, 'pineapple': 5, 'grape': 6}
print("-" * 100)
```

### Example 2: Handling Nested Dictionaries and Adding Complex Structures

```python
users_statuses = HashableDic()
online_status = {"status": "online"}
offline_status = {"status": "offline"}

user1 = {
    "id": 1,
    "name": "John",
    "age": 25,
    "location": {
        "city": "New York",
        "state": "NY",
        "country": "USA"
    }
}

user2 = {
    "id": 2,
    "name": "Jane",
    "age": 30,
    "location": {
        "city": "Los Angeles",
        "state": "CA",
        "country": "USA"
    }
}

# Adding users with their statuses
users_statuses.add(user1, online_status)
users_statuses.add(user2, offline_status)

# Updating statuses
users_statuses.add(user1, offline_status)
users_statuses.add(user2, online_status)

print(users_statuses)

# Attempting to add a dictionary with a different structure
# Raises ValueError: "Dictionary with different structure cannot be added."
users_statuses.add({"orange": 5})
```

In the second example, `HashableDic` can handle complex nested dictionaries and ensure that only structurally compatible dictionaries are added.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
