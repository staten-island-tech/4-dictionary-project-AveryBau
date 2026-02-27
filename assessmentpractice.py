
def occupied(n, y, t):
    found = 0
    for i in range (n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5, "CCCC.", "C...C")



""" def add(x,y):
    return x + y
result = add(5,6)
print(result)"""
