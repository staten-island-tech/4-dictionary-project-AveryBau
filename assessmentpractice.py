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

 
""" def language (sentence):
    t=0
    T=0
    s=0
    S=0
    for i in range (len(sentence)):
        if sentence[i] == "t" or sentence[i] == "T":
            t += 1
        if sentence[i] == "s" or sentence[i] == "S":
            s =+ 1
    print(s, t)
    if t > s:
        print("probably English")
    if s >= t:
        print("probably French")
language("The red cat sat on the mat. Why are you so sad cat? Don't ask that.") """


def honi(word):
    H = 0
    O = 0
    N = 0
    I = 0
    current = "H"
    HONI = 0
    for i in range (len(word)):
        if word[i] == current:
            H += 1
        if word[i] == current:
            O += 1
        if word[i] == current:
            N += 1
        if word[i] == current:
            I += 1
        if H+O+N+I == 4:
            HONI += 1
            H = 0
            O = 0
            N = 0
            I = 0
            current = "H"
            HONI == 0
    print(H, O, N, I, HONI)
honi("PROHODNIHODNIK")