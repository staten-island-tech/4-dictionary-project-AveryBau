best_buy_items = {    
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}

for index, item in enumerate(best_buy_items):
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

