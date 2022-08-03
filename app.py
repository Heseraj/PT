
# print("Hello World, Why my system doesn't work?")
# it is good to work wiht issues that really helps.

# print("Mosa Rahimi")
# print("o____")
# print(" ||||")
# print("*" * 10)
import math

# price = 10
# price = 20 # Integer number
# rating = 4.1 # floats
# name = "Mosa" # string
# is_published = True

# print(price)

# full_name = "John Smith"
# age = 20
# is_new_patient= True

# name = input("What is your name? ")
# print("Hi, " + name)


# name = input("What is your name? ")
# fav_color = input("What is your favorite Color? ")
# print(name + " likes " + fav_color)

# birth_year = input("birht year ")
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(age)
# print(type(age))

# full_name = input("What is your name? ")
# weight = input("how many pounds do you weight? " + full_name + " ")
# kilo_gram = int(weight)/ 2.2
# print("Ok " + full_name + "Your weight in Killogram is " + str(kilo_gram))


# course = "Python's Course for beginners"
# print(course)
# print(course[2:-2])
#
# multi_line = """Hello John.
# This is an example of our work.
# I would be very happy if you let me know how to work with it."""
# # print(multi_line)
# print(multi_line[0:5])
# print(multi_line[5:15])

#
# first_n = "John"
# last_n = "Smith"
# message = first_n + " [" + last_n + "] is a python pgoramer."
# print(message)

# first = "Mosa"
# last = "Rahimi"
# # formatted string,
# msg = f'{first} [{last}] is python coder.'
# print(msg)

course = "This Course is Python for Bigginers"
# print(len(course))
# course.upper()
# print(course.upper())
# print(course.lower())
# print(course.find("o"))
# print(course.replace("Bigginers", "Absolute Bigginners"))
# print(course.replace("bigginers", "Absolute Bigginners")) # Because the biggners term is not exactly with the variable
# print("Python" in course)
# print("python" in course)
# print(course.title())

# working with numbers and operatiors
# print(10*2)
# print(10+2)
# print(10/3)
# print(11//3)
# print(10**3)
# print(11%3)

# Augmented Assigned Operator
# x = 10
# x = x + 3
# x += 3
# print(x)

# Operation precednet (order of operations)
# y = 10 + 3 * 4 + 20 / 5
# print(y)
#
# x = (2 + 3) * 20 - 3
# print(x)

# z = 2.9
# print(z.__round__())
# print(z.__abs__())

import main
# z = 2.9
# print(math.ceil(z))
# print(math.floor(z))

# if statements in Python

# today = input("is today hot or cold? ")
#
# if today.lower() == "hot":
#     print("""Oh, it is a hot day.
#     Please make sure you dirnk plenty of whater.
#     enjoy your day :) """)
# if today.lower() == "cold":
#     print("""Oh, a cold day!
#     Please make sure you wear warm clothes.""")
# else:
#     print("It is a lovely day then")
# print("Enjoy your day.")

#  practice

# price = 10**6
# print(price)
# credit_score = input("is your credit good or poor? ")
# if credit_score.lower() == "good":
#     print(f" you need to pay 10 % of ${price} which is equal to ${0.1 * price}")
# if credit_score.lower() == "poor":
#     print(f" you need to pay 20 % of the ${price} which is equal to ${0.2 * price}")
# else:
#     print("""If your credit score is veyr poor, moderate or even excellent, Please talk to our financial representative!
#         we would like to do business with you.""")



# multiple if statements
#  if applicant has good credit and high income, then they are eligible for a house loan
#
# high_income = input("is your income high or true? ")
# credit_score = input("is your credit score is good? ")
# if high_income.lower() == "yes" or "true" or "high":
#     print("you might be eligible for a house loan. ")
# elif credit_score.lower() == "good" or "true" and high_income.lower() == "yes" or "true" or "high":
#     print("You are eligible to apply for a house loan")
# else:
#     print("""
#     Unfortunately, you are not eligible for an approved house loan.
#     Pleae set an appointment with a financial represntatives to evaluate your options.
#     """)

# example from course
# has_high_income = True
# has_high_credit = True
# has_criminal_record = False
#
# if has_high_credit and has_high_income and not has_criminal_record == True:
#     print("Congratulations! You are eligible for a house loan. ")
# else:
#     print("Please set an appointment with our financial representatives to evaluate your options")


# Contitional statments
# temperature = -5
# if temperature >= 30:
#     print("today is a hot day")
# elif temperature < 0:
#     print("today is a cold day")
# elif temperature < 30 and temperature > 10:
#     print("it is a moderate day")
# else:
#     print("today is a moderate day ")

# wegiht converstion
# y_weight = input("What is your weight? ")
# weight_unit = input("is your weight in Killogram K or in pounds L ")
#
# if weight_unit.upper() == "L":
#     print(f"your weight in Kilogram is equal to {float(y_weight) * 0.4536} Kg")
# elif weight_unit.upper() == "K":
#     print(f"your weight in pounds is equal to {float(y_weight) * 2.2}")
# else:
#     print("Pease choose the correction unit")


# using while loop
# i = 1
# while i <= 10:
#     print(i * 2 )
#     i += 1
# print("I Am Done")

# secret_num = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess_num = input("choose a number less than ten and you have only three chances! ")
#     guess_count += 1
#     if int(guess_num) == secret_num:
#         print("You won")
#         break
#     else:
#         print("sorry wrong number.")
#         if guess_count == 3:
#             print("This was your last chance. you failed! sorry :(")
#
# print("Next Person Please! ")


# for loops in Python mins 1:42

# for item in "python":
#     print(item)
#
# for item in range(10):
#     print(item)
#
# for item in range (2, 10, 2):
#     print(item)

# items_prince = [10, 15, 14, 20, 11]
# total = 0
# for price in items_prince:
#     total += price
# print(f"your total amount is {total}.")

# Nested loops in Python
# for x in range(4):
#     for y in range(4):
#         print(f" ({x} , {y})")

numbers = [5, 2, 5, 2, 2, 2]
# for number in numbers:
#     # print(number)
#     print(f'{"*"* number}')
x = 0
for number in numbers:
    output = ""
    for count in range(number):
        output += "X"
        # print(output)
    print(output)