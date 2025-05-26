fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: orange
print(fruits[2])  # Output: cherry
print(len(fruits))  # Output: 3
fruits.append("orange")  # Add an item to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")  # Remove the item "banana" from the list
print(fruits)  # Output: ['apple', 'cherry', 'orange']
fruits.pop(1)  # Remove the item at index 1 (which is "cherry")
print(fruits)  # Output: ['apple', 'orange']