my_list = []

# Add numbers to the list
for num in (10, 20, 30, 40):
    my_list.append(num)
print(my_list)

# Insert 15 at the second position
my_list.insert(1, 15)
print(my_list)

# Extend with another list
list_two = [50, 60, 70]
my_list.extend(list_two)
print(my_list)

# Remove the last element
my_list.pop()
print(my_list)

# Sort the list in ascending order
my_list.sort()

# Find index of value 30
position = my_list.index(30)
print("index of value 30:", position)
