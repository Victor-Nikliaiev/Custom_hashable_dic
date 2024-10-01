# HashableDic Class

## Overview

`HashableDic` is a Python class designed to provide a dictionary that is hashable. This allows the dictionary to be used as a key in another dictionary or as an element in a set, making it useful for situations where the immutability of a dictionary is required, but you still want to allow for modification of its contents in a controlled way.

### Features

-   Can add key-value pairs or whole dictionaries.
-   Supports both mutable and immutable behaviors.
-   Provides equality and hashing capabilities to allow usage as a key in dictionaries or elements in sets.
-   Ensures that dictionaries with different structures cannot be added to the existing dictionary.

## Installation

Clone the repository or download the `HashableDic` class file and include it in your project:

```bash
git clone <repository-url>
```

Ensure that your project follows the [MIT License](LICENSE.md) conditions, provided with this project.

## Usage

Below is an example of how to use the `HashableDic` class:

```python
# Example usage of HashableDic

# Create a HashableDic instance
fruits = HashableDic({
    "apple": 1,
    "orange": 2,
    "banana": 3
})

# Add more fruits
fruits.add({
    "mango": 4,
    "pineapple": 5
})

# Add another key-value pair
fruits.add("grape", 6)

# Print the updated dictionary
print(fruits)

# Working with more complex dictionaries
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

# Add users with statuses
users_statuses.add(user1, online_status)
users_statuses.add(user2, offline_status)

# Update statuses
users_statuses.add(user1, offline_status)
users_statuses.add(user2, online_status)

# Print the updated user statuses
print(users_statuses)
```

### Methods

-   `add(*args)`: Adds key-value pairs or dictionaries to the `HashableDic`.
-   `remove(key)`: Removes a key-value pair from the dictionary.
-   `get(key)`: Retrieves a value by its key.
-   `__getitem__(key)`: Retrieves a value by key using the `[]` operator.
-   `__setitem__(key, value)`: Sets a value for a given key using the `[]` operator.
-   `__contains__(key)`: Checks if a key exists in the dictionary.
-   `__iter__()`: Allows iteration over the dictionary's items.
-   `__eq__(other)`: Compares two `HashableDic` objects for equality.
-   `__hash__()`: Returns the hash value of the dictionary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.
