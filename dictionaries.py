# Dictionaries => key-value pairs
# Dictionaries does not guarantee order

person1 = {"first": "Christopher"}
person1["last"] = "Harrison"
print(person1)
print(person1["first"])
print()

person2 = {"first": "Brian"}
person2["last"] = "Mathenge"
print(person2)

print()

people = []
people.append(person1)
people.append(person2)
print(people)