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
prices = []
purchase = ""
money = ""

while purchase != 'done':
    purchase ==input("What would you like to buy? (say 'done' to stop)")
    cart.append(purchase)
    money = float(input("give cost (type '0' to finish)"))
    prices.append(money)
if 'done':
    input("Are you done with your purchase?")
elif 'yes':
    input("Someone's a lil' stingy...but thank you I guess")
elif 'no': 
    input("GOOD whatchu want?")
    cart.append(purchase)
    money = float(input("Give cost"))
    prices.append(money)
print(cart, prices)
total = sum(prices)

print(cart, total)

    
    




