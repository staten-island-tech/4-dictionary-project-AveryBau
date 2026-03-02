""" 
def occupied(n, y, t):
    found = 0
    for i in range (n):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
occupied(5, "C.C.C", "C..CC") """




""" def add(x,y):
    return x + y
result = add(5,6)
print(result)"""


def languages (sentence):
    t=0
    T=0
    s=0
    S=0
    for i in range (sentence):
        if sentence[i] == "t":
            t += 1
        if sentence[i] == "T":
            T += 1
        if sentence[i] == "s":
            s =+ 1
        if sentence[i] == "S":
            S =+ 1
    if s+S >= t+T:
        print("probably English")
    if t+T >= s+S:
        print("probably French")
languages(3, "The red cat sat on the mat. Why are you so sad cat? Don't ask that.")