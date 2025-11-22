
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Original list:", fruits)


fruits.append("kiwi")
print("After appending one fruit:", fruits)


fruits.extend(["grape", "papaya"])
print("After extending with multiple fruits:", fruits)


fruits.insert(2, "pineapple")
print("After inserting at position 2:", fruits)

fruits_pop = fruits.copy()
fruits_pop.pop(2)
print("After pop() at index 2:", fruits_pop)


fruits_remove = fruits.copy()
fruits_remove.remove(fruits_remove[2])
print("After remove() third element:", fruits_remove)


fruit_to_find = "banana"
index = fruits.index(fruit_to_find)
count = fruits.count(fruit_to_find)
print(f"Index of '{fruit_to_find}':", index)
print(f"Count of '{fruit_to_find}':", count)


fruits.reverse()
print("Reversed list:", fruits)

fruits.sort()
print("Sorted alphabetically:", fruits)
