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
loop = True
asking_name = True


def mark_answer(answer):
    global points
    global num_correct_ans
    if answer in answer_list:
        points += 10
        num_correct_ans += 1
        print("\033[1;32mCorrect!\033[0m")
        print("\033[1;37mYou have {} points!\033[0m".format(points))
    else:
        print("\033[1;31mWrong!\033[0m")
        print("\033[1;37mYou have {} points!\033[0m".format(points))
        pass

    return (points, num_correct_ans)

# ------------------ Main program ------------------ #
# asking users name using input
print(
    "\n\033[1;37mThis quiz will test your knowledge on Level 2 Calculus. "
    "You will start with 0 points.\n"
   ) 
#4 second pause
time.sleep(4)
print(
   "\033[1;37mIf you get an answer \033[1;32mRight\033[1;37m, " 
   "you gain 10 points but if you get an answer \033[1;31mWrong\033[1;37m, " 
   "you will not lose or gain any points.\n"
)
# 4 second pause
time.sleep(4)
print(
    "\033[4;31m\033[1;31mRules:\033[0m\033[1;37m\n- When answering questions " 
    "with a power, use '^'.\n"
)
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

# asks user their name
while asking_name:
    name = str(input("\033[1;37mWhat is your name?\n Name: ")).title()
    if len(name) > 0:
        print("\nNice to meet you {}, good luck on this quiz!".format(name))
        asking_name = False
    else:
        print("\033[1;31m\nPlease enter a name!\033[0m")
        time.sleep(0.5)
        continue

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
print("1\033[0m")
# 1 second pause
time.sleep(1)

while loop:
    # Q1 - Differentiation
    print('\033[1;34m\nQuestion 1:\033[0m')
    print("\033[1;36mDifferentiate the function f(x)= x^3+2x^2-x+6")
    answer = str(input("f'(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q2 - Differentiation
    print('\033[1;34m\nQuestion 2:\033[0m')
    print("\033[1;36mDifferentiate the function f(x) = 1/3x^3-1/2x^2+x-1")
    answer = str(input("f'(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q3 - Differentiation
    print('\033[1;34m\nQuestion 3:\033[0m')
    print("\033[1;36mDifferentiate the function f(x) = 4/2x^3+6/3x^2-7x-9")
    answer = str(input("f'(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q4 - Differentiation
    print('\033[1;34m\nQuestion 4:\033[0m')
    print("\033[1;36mDifferentiate the function f(x) = 20/2x^3-15/3x^2-x+18")
    answer = str(input("f'(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q5 - Differentiation
    print('\033[1;34m\nQuestion 5:\033[0m')
    print("\033[1;36mDifferentiate the function f(x) = 60/3x^2-15x+3")
    answer = str(input("f'(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

print(
    "\033[1;37m\nThe following 5 questions will test you on Level 2 "
    "Integration skills\n"
)
#3 second pause
time.sleep(4)
print("You must give the answer with the constant value +c!\n")
#3 second pause
time.sleep(3)
print("Good luck!\033[1;36m")

while loop:
    # Q6 - integration
    print('\033[1;34m\nQuestion 6:\033[0m')
    print("\033[1;36mIntegrate the function f'(x) = 4x-12 where f(5) = 12")
    answer = str(input("f(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q7 - integration
    print('\033[1;34m\nQuestion 7:\033[0m')
    print("\033[1;36mIntegrate the function f'(x) = 8x^3-3x^2+14 where f(2) = 20")
    answer = str(input("f(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q8 - integration
    print('\033[1;34m\nQuestion 8:\033[0m')
    print("\033[1;36mIntegrate the function f'(x) = 6x^2-2x+4 where f(2) = 5")
    answer = str(input("f(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q9 - integration
    print('\033[1;34m\nQuestion 9:\033[0m')
    print("\033[1;36mIntegrate the function f'(x) = x^2-5x+1 where f(2) = 5")
    answer = str(input("f(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

while loop:
    # Q10 - integration
    print('\033[1;34m\nQuestion 10:\033[0m')
    print("\033[1;36mIntegrate the function f'(x) = 108x^3-48x^2-18x+4 where f(2) = 216")
    answer = str(input("f(x) = \033[0m"))
    if len(answer) > 0:
        mark_answer(answer)
        break
    else:
        print("\033[1;31m\nPlease enter an answer!\033[0m")
        print(
        "\033[1;35mEnter any character "
        "if you dont know the answer\033[0m"
        )
        continue

# 2 second pause
time.sleep(2)
print("\033[1;31m\nQUIZ HAS ENDED {}\033[0m".format(name))
# 3 second pause 
time.sleep(3) 
print("\033[1;33mloading score")
# 1 second pause
time.sleep(1)
print("loading score.")
# 0.1 second pause
time.sleep(0.1)
print("loading score..")
# 0.5 second pause
time.sleep(0.5)
print("loading score...\033[0m")
time.sleep(1)
# If, elif and else statement 
if num_correct_ans >= 7 and num_correct_ans <=10:
    print(
        "\033[1;32mGood job! {}"
        "You scored {} out of 10".format(name, num_correct_ans)
    )
    print("Total points earned: {}\033[0m".format(points))
elif num_correct_ans >= 3 and num_correct_ans <= 6:
    print(
        "\033[1;33mYou did okay {}. You scored {} out of 10"
        .format(name, num_correct_ans)
    )
    print("Total points earned: {}\033[0m".format(points))
else:
    print(
        "\033[1;31mYou failed {}. "
        "You scored {} out of 10. I am disappointed"
        .format(name, num_correct_ans)
    )
    print("Total points earned: {}\033[0m".format(points))
