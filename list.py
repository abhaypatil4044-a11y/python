s = " Python Programming is FUN "


stripped = s.strip()
print("Stripped:", stripped)

lower = stripped.lower()
print("Lowercase:", lower)

upper = stripped.upper()
print("Uppercase:", upper)


is_count = stripped.count("is")
print("Count of 'is':", is_count)


index_prog = stripped.find("Programming")
print("Index of 'Programming':", index_prog)


replaced = stripped.replace("FUN", "Awesome")
print("Replaced:", replaced)


words = stripped.split()
hyphen_joined = "-".join(words)
print("Hyphen joined:", hyphen_joined)


starts_with = stripped.startswith("Python")
ends_with = stripped.endswith("FUN")
print("Starts with 'Python':", starts_with)
print("Ends with 'FUN':", ends_with)
