from custom_hashable_dictionary import HashableDic

##################################################
print("-"*100)
fruits = HashableDic({
    "apple": 1,
    "orange": 2,
    "banana": 3
})

fruits.add({
    "mango": 4,
    "pineapple": 5})  

fruits.add("grape", 6)
print(fruits)
print("-"*100)
##################################################

users_statuses = HashableDic()
online_status = {"status" : "online"}
offline_status = {"status" : "offline"}

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

users_statuses.add(user1, online_status)
users_statuses.add(user2, offline_status)

users_statuses.add(user1, offline_status)
users_statuses.add(user2, online_status)
users_statuses.add({"orange": 5})  # Raises ValueError: "Dictionary with different structure cannot be added."
print(users_statuses)




 

