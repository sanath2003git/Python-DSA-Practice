products = [
    ("Laptop", 50000),
    ("Mouse", 1000),
    ("Keyboard", 3000),
    ("Monitor", 50000)
]

products.sort(key=lambda x: (x[1], x[0]))

print(products)