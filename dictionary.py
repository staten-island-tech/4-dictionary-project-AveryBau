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
    "description": "Cow juice"
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


print("WELCOME TO AVERY'S GROCERY STORE!!!")

for index, item in enumerate(grocery_store):
    print(index, ":", item["name"], item["price"])

cart = []
total = 0

purchase = int(input("What would you like to buy? (Type in the number of item)"))
cart.append(grocery_store[purchase])
print(cart)
total += grocery_store[purchase]["price"]

while True:
    checkout = input("Do you wish to continue shopping? (type yes or no)")
    if checkout =="yes":
        purchase = int(input("What else would you like to buy?"))
        cart.append(grocery_store[purchase])
        print(cart)
        total += grocery_store[purchase]["price"]
    elif checkout == "no":
        break
for item in cart:
    print(f"{(item["name"])}, ${float(item["price"])}")
print(f"Total: ${total}")

    

    
    




