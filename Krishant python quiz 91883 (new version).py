import time

# Creating lists and variables
# Initial points equal to zero 
points = 0
# declaring answer list 
answer_list = [
    "3x^2+4x-1", "x^2-x+1", "6x^2+4x-7", "30x^2-10x-1", "40x-15",
    "2x^2-12x+22", "2x^4-x^3+14x-32","2x^3-x^2+4x-15", 
    "x^3/3-5x^2/2+x+31/3", "1/3x^3-5/2x^2+x+31/3", "27x^4-16x^3-9x^2+52"
    ]
answer = ""
num_correct_ans = 0

def mark_answer(answer):
    global points
    global num_correct_ans
    if answer in answer_list:
        points += 10
        num_correct_ans += 1
        print("\033[1;32mCorrect!\033[1;37m")
        print("You have {} points!\033[1;36m".format(points))
    else:
        print("\033[1;31mWrong!\033[1;37m")
        print("You have {} points!\033[1;36m".format(points))

    return (points, num_correct_ans)

# ------------------ Main program ------------------ #
# asking users name using input
print("\n\033[1;37mThis quiz will test your knowledge on Level 2 Calculus. You will start with 0 points.\n") 
#4 second pause
time.sleep(4)
print("\033[1;37mif you get an answer \033[1;32mRight\033[1;37m, you gain 10 points but if you get an answer \033[1;31mWrong\033[1;37m, you will not lose or gain any points.\n")
# 4 second pause
time.sleep(4)
print("\033[4;31m\033[1;31mRules:\033[0m\033[1;37m\n- When answering questions with a power, use '^'.\n")
# 2 second pause
time.sleep(2)
print("- When answering questions with a fraction, use '/'.\n")
# 2 second pause
time.sleep(2)
print("- You are allowed to use a calculator to answer these questions.\n")
# 2 second pause
time.sleep(2)
print("- Remember to include the C value in Integration questions.\n")
# 5 second pause
time.sleep(5)
name = input("\033[1;37mWhat is your name?\n name:")
print("\nNice to meet you {}, good luck on this quiz!".format(name))
# 3 second pause
time.sleep(3)
print("The quiz starts in:")
# 1 second pause
time.sleep(1)
print("\033[1;32m3")
# 1 second pause
time.sleep(1)
print("2")
# 1 second pause
time.sleep(1)
print("1")
# 1 second pause
time.sleep(1)

# Q1 - Differentiation
print('\033[1;36m\nQuestion 1:')
print("Differentiate the function f(x)= x^3+2x^2-x+6")
answer = str(input("f'(x) = "))
mark_answer(answer)

# Q2 - Differentiation
print('\nQuestion 2:')
print("Differentiate the function f(x) = 1/3x^3-1/2x^2+x-1")
answer = str(input("f'(x) = "))
mark_answer(answer)

# Q3 - Differentiation
print('\nQuestion 3:')
print("Differentiate the function f(x) = 4/2x^3+6/3x^2-7x-9")
answer = str(input("f'(x) = "))
mark_answer(answer)

# Q4 - Differentiation
print('\nQuestion 4:')
print("Differentiate the function f(x) = 20/2x^3-15/3x^2-x+18")
answer = str(input("f'(x) = "))
mark_answer(answer)

# Q5 - Differentiation
print('\nQuestion 5:')
print("Differentiate the function f(x) = 60/3x^2-15x+3")
answer = str(input("f'(x) = "))
mark_answer(answer)

print("\033[1;37m\nThe following 5 questions will test you on Level 2 Integration skills\n")
#3 second pause
time.sleep(4)
print("You must give the answer with the constant value +c!\n")
#3 second pause
time.sleep(3)
print("Good luck!\033[1;36m\n")

# Q6 - integration
print('\nQuestion 6:')
print("Integrate the function f'(x) = 4x-12 where f(5) = 12")
answer = str(input("f(x) = "))
mark_answer(answer)

# Q7 - integration
print('\nQuestion 7:')
print("Integrate the function f'(x) = 8x^3-3x^2+14 where f(2) = 20")
answer = str(input("f(x) = "))
mark_answer(answer)

# Q8 - integration
print('\nQuestion 8:')
print("Integrate the function f'(x) = 6x^2-2x+4 where f(2) = 5")
answer = str(input("f(x) = "))
mark_answer(answer)

# Q9 - integration
print('\nQuestion 9:')
print("Integrate the function f'(x) = x^2-5x+1 where f(2) = 5")
answer = str(input("f(x) = "))
mark_answer(answer)

# Q10 - integration
print('\nQuestion 10:')
print("Integrate the function f'(x) = 108x^3-48x^2-18x+4 where f(2) = 216")
answer = str(input("f(x) = "))
mark_answer(answer)

# 2 second pause
time.sleep(2)
print("\033[1;31mQUIZ ENDS\033[1;32m")
# 3 second pause 
time.sleep(3) 
print("loading score")
# 1 second pause
time.sleep(1)
print("loading score.")
# 0.1 second pause
time.sleep(0.1)
print("loading score..")
# 0.5 second pause
time.sleep(0.5)
print("loading score...")
# 2 second pause 
time.sleep(2)
print("loading score")
# 3 second pause 
time.sleep(3)
print("loading score.")
# 0.4 second pause 
time.sleep(0.4)
print("loading score..")
# 0.1 second pause 
time.sleep(0.1)
print("loading score...")

# If, elif and else statement 
if num_correct_ans >= 7 and num_correct_ans <=10:
    print(
        "\033[1;32mGood job!"
        "You scored {} out of 10".format(num_correct_ans)
    )
elif num_correct_ans >= 3 and num_correct_ans <= 6:
    print("\033[1;33mYou did okay. You scored {} out of 10".format(num_correct_ans))
else:
    print("\033[1;31mYou completely failed. You scored {} out of 10. I am dissapointed".format(num_correct_ans))



