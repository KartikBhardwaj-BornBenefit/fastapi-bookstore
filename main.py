
# Example 1: append vs extend
fruits = ['apple', 'banana']
vegetables = ['carrot', 'tomato']

# Using append
fruits.append(vegetables)
print("After append:", fruits)  # Output: ['apple', 'banana', ['carrot', 'tomato']]

# Using extend
fruits = ['apple', 'banana']  # Reset list
fruits.extend(vegetables)
print("After extend:", fruits)  # Output: ['apple', 'banana', 'carrot', 'tomato']

# Example 2: + operator vs extend
list1 = [1, 2, 3]
list2 = [4, 5]

# Using + operator (creates new list)
result = list1 + list2
print("Original list1:", list1)  # Output: [1, 2, 3]
print("After + operator:", result)  # Output: [1, 2, 3, 4, 5]

# Using extend (modifies original)
list1.extend(list2)
print("After extend:", list1)  # Output: [1, 2, 3, 4, 5]

# Example 3: append with single item vs list
numbers = [1, 2, 3]
numbers.append(4)  # Adding single item
print("Append single item:", numbers)  # Output: [1, 2, 3, 4]

numbers.append([5, 6])  # Adding list as single item
print("Append list:", numbers)  # Output: [1, 2, 3, 4, [5, 6]]
