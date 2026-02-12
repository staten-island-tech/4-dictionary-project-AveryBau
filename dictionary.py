pals = [
{
    "name": "Sophie",
    "price": 6767.67,
    "department": "history museum",
    "description": "balls."
},
{
    "name": "Sabrina",
    "price": 333.00,
    "department": "Yuri",
    "description": "bark bark"
},
]


print(pals[0]["name"])

for index, item in enumerate(pals):
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




