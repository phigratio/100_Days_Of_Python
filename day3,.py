# print("Welcome to the rollercoaster")
# height=int(input("What is your height?"))
# if height>120:
#      print("You can ride the rollercoaster")
#      age=int(input("What is your age?"))
#      if age>=18:
#        print("Please pay 12 dollars")
#      elif age<=18 and age >=12:
#        print("please pay 10 dollars")
#      else:
#        print("please pay 7 dollars")
# else:
#      print("You have to grow taller")

# number=int(input("Which number do u want to check?"))
# if (number%2)==0:
#   print("the number is even")
# else:
#   print("The number is odd")
# height=float(input("Enter your height"))
# weight=float(input("Enter your weight"))
# bmi=round(weight/(height**2))1.8
# if bmi<18.5:
#     print("youre underweight")
# elif bmi>=18.5 and bmi<=25:
#     print(bmi)
#     print("You are moderate")
# elif bmi>25 and bmi<=30:
#     print(bmi)
#     print("you are overweight")
# elif bmi>30 and bmi<=35:
#     print(bmi)
#     print("You are obese")
# else :
#     print(bmi)
#     print("You are clinically obese")
#
# print("Welcome to the roller coaster!")
# height=int(input("Enter your height"))
# if height>120:
#     age=int(input("Enter your age"))
#     if age<12:
#         bill=5
#         photo=input("Do u want a photo")
#         if photo=="Yes" or photo=="yes":
#             bill=bill+3
#             print(f"your bill is {bill}")
#         else:
#             print(f"your bill is {bill}")
#     elif age>=12 and age<18:
#         bill = 7
#         photo = input("Do u want a photo?")
#         if photo == "Yes" or photo == "yes":
#             bill = bill + 3
#             print(f"your bill is {bill}")
#         else:
#             print(f"your bill is {bill}")
#     else:
#         bill = 12
#         photo = input("Do u want a photo")
#         if photo == "Yes" or photo == "yes":
#             bill = bill + 3
#             print(f"your bill is {bill}")
#         else:
#             print(f"your bill is {bill}")
# else:
#     print("Sorry not eligible for riding")
# print("Welcome to the Pizza store")
# size=input("Enter the size of Pizza.Type S L or M")
# pepperoni=input("Do u want extra pepperoni? Y or N")
# cheese=input("Do u want extra cheese?Y or N")
# if size=="S":
#     bill=15
#     if pepperoni=="Y":
#         bill+=2
#         if cheese=="Y":
#             bill+=1
#     else:
#         if cheese=="Y":
#             bill+=1
# if size=="M":
#     bill=20
#     if pepperoni=="Y":
#         bill+=3
#         if cheese=="Y":
#             bill+=1
#     else:
#         if cheese=="Y":
#             bill+=1
# if size=="L":
#     bill=25
#     if pepperoni=="Y":
#         bill+=3
#         if cheese=="Y":
#             bill+=1
#     else:
#         if cheese=="Y":
#             bill+=1
# print(f"Your bill is {bill}")
# print("Welcome to the love calculator")
# name1=input("Enter your name").lower()
# name2=input("Enter your loves name").lower()
# count1=name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")
# count2=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
# ans=count2*10+count1
# print(f"{ans} is your love percentage")
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the treasure island\nYour mission is to find the treasure")
direction=input("Which direction do u want to go.Left or Right")
if direction=="left":
    swim=input("Do u want to swim or wait")
    if swim=="wait":
        door=input("Which door")
        if door=="Yellow":
            print("You Win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("game Over")


