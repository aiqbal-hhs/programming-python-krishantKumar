x = 0
score = x
print("This quiz is about Algebra! You need to answer by writing what letter you think the answer is. This is an algebra revision quiz, good luck!")
# Question One 
print("What is Algebra?")
answer_1 = input("a)Maths which involves the use of algorithm\nb)Maths that involve the use of letters in formula or equations.\nc)Maths involving triangles.\n:")
if answer_1.lower() == "b" or answer_1.lower() == "Maths that involve the use of letters in formula or equations.":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect")

# Question Two
print("Solve x + 5 = 10")
answer_2 = input("a)X = 15\nb)X = 10\nc)X = 5\n:")
if answer_2.lower() == "c" or answer_2.lower() == "x = 5":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Three
print("Solve 3x + 6 = 15")
answer_3 = input("a)X = 7\nb)X = 6\nc)None of the above\n:")
if answer_3.lower() == "c" or answer_3.lower() == "None of the above":
    print("Correct")
    x = x + 1

# Question Four
print("Factorise: x² - 5x + 6")
answer_4 = input("a)(x - 2)(x - 3)\nb)(x +2)(x + 3)\nc)(x - 2)(x + 3)\n:")
if answer_4.lower() == "a" or answer_4 == "(x - 2)(x - 3)":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Five
print("Solve: 2x² - 11x + 14 = 0")
answer_5 = input("a)X = -4 or X = -7\nb)X = -4 or X = 7\nc)None of the above\n:")
if answer_5.lower() == "a" or answer_5 == "X = -4 or X = -7":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question six
print("Expand: (x + 20)(5x + 40) + 5")
answer_6 = input("a)5x² + 140x + 805\nb)5x² - 140x + 805\nc)5x² - 140x - 805\n:")
if answer_6.lower() == "a" or answer_6 == "5x² + 140x + 805":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Seven
print("Solve: 5ˣ = 65")
answer_7 = input("a)X = 10\nb)X = -13\nc)X = 13\n:")
if answer_7.lower() == "c" or answer_7 == "X = 13":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Eight
print("Solve: y² - 106x + 505 = 0")
answer_8 = input("a)Y = 5 or y = 101\nb)Y = -5 or y = -101\nc)None of the above\n:")
if answer_8.lower() == "b" or answer_8 == "Y = -5 or y = -101":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Nine
print("Who made algebra?")
answer_9 = input("a)Al-Khwarizmi\nb)Al-Yousef\nc)Albert Einstein\n:")
if answer_9.lower() == "a" or answer_9 == "Al-Khwarizmi":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

# Question Ten
print("Is algebra important to know?")
answer_10 = input("a)Yes\nb)No\nc)Maybe\n:")
if answer_10.lower() == "a" or answer_10 == "Yes":
    print("Correct")
    x = x + 1
else:
    print("Incorrect")

#Total Score
score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")
print("WELL DONE!!!")
