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

""" def showItems(items):
    for index, item in enumerate(items):
            print(index, ":", item['name'])

def thing():
        showItems(grocery_store)
        x = int(input("buy?"))
        print(grocery_store[x])
showItems(grocery_store)
print(grocery_store[0])
thing()
 """

for index, item in enumerate(grocery_store):
    print(index, ":", item["name"], item["price"])

cart = []
prices = []
purchase = ""

while purchase != 'done':
    purchase == int(input("buy?"))
    cart.append(grocery_store)
    print(grocery_store[purchase])
if 'done':
    input("Are you done with your purchase?")
elif 'yes':
    input("Thank you for your purchase")
    print(cart, prices)
    total = sum(prices)
elif 'no':
    purchase != 'done'

print(cart, total)

    
    




