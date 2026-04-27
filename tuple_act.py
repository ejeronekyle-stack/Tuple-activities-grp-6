# Activity 1: Access Elements
colors = ("red", "green", "blue")
print("First item:", colors[0])
print("Last item:", colors[-1])

# Activity 2: Slicing
numbers = (10, 20, 30, 40, 50)
print("Slice (20, 30, 40):", numbers[1:4])

# Activity 3: Tuple Methods
nums = (1, 2, 2, 3, 2)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

# Activity 4: Tuple Packing & Unpacking
point = (5, 10)
x, y = point
print("x =", x, ", y =", y)

# Activity 5: Combine Tuples
t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2
repeated = combined * 2
print("Combined:", combined)
print("Repeated twice:", repeated)
