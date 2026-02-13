grocery_store = [
{
    "name": "Apples",
    "price": 3.50,
    "department": "Fruit",
    "description": "Keeps the doctors away"
},
{
    "name": "Milk",
    "price": 7.00,
    "department": "Dairy",
    "description": "Came from a cow"
},
{
    "name": "Chips",
    "price": 6.60,
    "department": "Snack",
    "description": "Crunchy and totally healthy"
},
{
    "name": "Bread",
    "price": 7.50,
    "department": "Grains",
    "description": "Good carbs"
},
{
    "name": "Cookies",
    "price": 6.99,
    "department": "Sweet Treats",
    "description": "Yummy sugar"
},
{
    "name": "Lettuce",
    "price": 5.25,
    "department": "Vegetables",
    "description": "Tasteless Health"
},
{
    "name": "Beef",
    "price": 9.00,
    "department": "Protein",
    "description": "MEAT",
},


]


print(grocery_store[0]["name"])

for index, item in enumerate(grocery_store):
    print(index, ":", item["name"])





"""If you want just the name of the first item, you write:"""
""" best_buy_items[0]["name"] """
""" [0] means the first item in the list
["name"] means “look inside that dictionary and grab the name. """

""" If you want the price of the second item:
best_buy_items[1]["price"] """
""" 
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])

index: the position in the list (0, 1, 2, 3, …).
item: the dictionary at that position. """




