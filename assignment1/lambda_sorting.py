# List of tuples containing names and ages
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 20)]

# Sort the list in descending order of age using a lambda function
sorted_people = sorted(people, key=lambda person: person[1], reverse=True)
print(sorted_people)
# Print the sorted list
print("Sorted list in descending order of age:")
for name, age in sorted_people:
    print(f"{name}: {age}")
