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
    "price": 6.70,
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
    "department": "Meat",
    "description": "PROTEIN",
},

]


print("WELCOME TO AVERY'S GROCERY STORE!!! PLS BUY SMTH IM BROKE")

for index, item in enumerate(grocery_store):
    print(index, ":", item["name"], item["price"])

cart = []
total = 0
purchase = ""

found = False
for items in grocery_store:
    if purchase == items["name"]:
        cart.append(items)
        total += items["price"]
    done = input("What would you like to buy?")
    found = True
    done = input("Are you done with your purchase?")
    if done == "no":
        purchase = input("What would you like to buy?")
        found = True
    elif done == "yes":
        print("Someone's a lil' stingy...")
    
for items in cart:
    print("-", item)
    print("Total: $", total)

    
    




