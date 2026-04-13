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


""" def honi(word):
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
        else:
            HONI == 0
    print(HONI)
honi("MAGNUS")
honi("HHHHOOOONNNNIIII")
honi("PROHODNIHODNIK") """


""" def magnus(word):
    count = 0
    state = 0

    for char in word: 
        if state == 0 and char.upper() == "H":
            state = 1
        elif state == 1 and char.upper() == "O":
            state = 2
        elif state == 2 and char.upper() == "N":
            state = 3
        elif state == 3 and char.upper() == "I":
            state = 0
            count += 1
    print(count)
magnus("HHHHOOOONNNNIIII")
magnus("MAGNUS")
magnus("PROHODNIHODNIK") """


""" def multiplechoice(number, answers, correct):
    right = 0
    for i in range(len(answers)):
        if answers[i] == correct[i]:
            right += 1
    print(right)
multiplechoice(3, "AAB", "AAC") """


""" def uncrackable(password):
    U = 0
    L = 0
    D = 0
    for i in range(len(password)):
        if password[i] == "upper":
            U += 1
        elif password[i] == "lower":
            L += 1
        elif password[i] == "digit":
            D += 1
    if U >= 3 or L >= 2 or D >= 1:
        print("Valid")
    else: 
        print("Invalid")
    if password <= 12 or password >= 8:
        print("Valid")
    else:
        print("Invalid")
uncrackable("PassW0rd") """


""" def Tarifa(megabits, number_months, usage):
    value = 0
    for use in usage:
        value += megabits
        value -= use
    print(value + megabits)
Tarifa(10, 3, [4,6,2])
 """
""" def Tarifa(megabits, number_months, usage):
    value = 0
    for i in range(number_months):
        value += megabits
        value -= i
    print(value + megabits)
Tarifa(10, 3, [4,6,2]) """


""" def slot(total, first, second, third):
    times = 0
    quarters = total
    slotuno = 35 - first
    slotdos = 100 - second
    slottres = 10 - third
    while quarters > 0:
        quarters -= 1
        slotuno -= 1
        times += 1
        if quarters == 0:
            print(times)
        quarters -= 1
        slotdos -= 1
        times += 1
        if quarters == 0:
            print(times)
        quarters -= 1
        slottres -= 1
        times += 1
        if quarters == 0:
            print(times)
        if slotuno == 0:
            quarters += 30
            slotuno += 35
        if slotdos == 0:
            quarters += 60
            slotdos += 100 
        if slottres == 0:
            quarters += 9
            slottres += 10
    if quarters == 0:
        print(times)
slot(48, 3, 10, 4)
slot(77, 4, 9, 3)
 """

