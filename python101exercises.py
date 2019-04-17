# Assignment 1 and 2:

# name = input("What is your name?")

# count = len(name)

# print("Hello".upper() + name.upper())

# sentence = 'Your name has %s letters!' % (count)

# print(sentence.upper())


# Assignment 3:

# print("Fill in the blanks below.")
# print("Why did the ___ cross the road?")

# x = input("What crossed the road?")

# print("Why did the" + x + " cross the road?")

# Assignment 4:
# day = int(input('Day (0-6)? ')) # Fill in your code here

# if day == 0:
#     print ("Sunday")
# elif day == 1:
#     print ("Monday")
# elif day == 2:
#     print ("Tuesday")
# elif day == 3:
#     print ("Wednesday")
# elif day == 4:
#     print ("Thursday")
# elif day == 5: 
#     print ("Friday")
# elif day == 6:
#     print ("Saturday")

#Assignment 5:

# day = int(input('Day (0-6)?'))

# if day < 5:
#     print ("Go to work")
# else:
#     print ("Sleep In")

#Assignment 6:

# print("What is the temperature in Celsius?")

# x = input("Enter the temperature: ")

# fahrenheit = int(x) * 1.8 + 32

# print (fahrenheit)

# Assignment 7:

# total_bill = float(input("Enter total bill amount: "))
# service_level = str(input("Enter level of service from good, fair or bad: "))


# if service_level == "good":
#     tip_amount = total_bill * .20
# elif service_level == "fair":
#     tip_amount = total_bill * .15
# elif service_level == "bad":
#     tip_amount = int(total_bill) * .10

# total_amount = total_bill + tip_amount

# print ("${:.2f}".format(total_amount))

# Assignment 8:
# total_bill = float(input("Enter total bill amount: "))
# service_level = str(input("Enter level of service from good, fair or bad: "))
# number_of_people = int(input("How many people in your group?: "))


# if service_level == "good":
#     tip_amount = total_bill * .20
# elif service_level == "fair":
#     tip_amount = total_bill * .15
# elif service_level == "bad":
#     tip_amount = int(total_bill) * .10

# total_amount = total_bill + tip_amount
# per_person = total_amount / number_of_people

# print ("${:.2f}".format(total_amount))
# print ("${:.2f}".format(per_person))

# Assignment 9:
# x = 0
# while x < 10:
#     x += 1
#     print(x)

# Assignment 10:
# coins = 0
# while True:
#     answer = input("Do you want a coin?: ")
#     if answer.lower() == "yes":
#         coins = coins + 1
#         print("You have " + str(coins) + " coins")
#     if answer.lower() == "no":
#         break
# print("Bye")     