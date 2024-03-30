#print("Hello"[3])
#print(123+345)
#print(len("Hello"))
# num_char=len(input("What is your name?"))
# new_num_char=str(num_char)
# print("Your name has "+ new_num_char + " characters")
# print(str(70)+str(100))
# print(float("100")+70.5)
# type_two_digit_number=input("What is the number?")
# first_digit=type_two_digit_number[0]
# second_digit=type_two_digit_number[1]
# result=int(first_digit)+int(second_digit)
# print(result)
# age=input("What is your current age")
# remain=90-int(age)
# days=remain*365
# months=remain*12
# week=remain*52
# print(f"you have {days} days,{week} weeks,{months} months")
print("Welcome to the tip calculator")
bill=input("What was thr bill?")
tip=input("What percentage tip would you like to give?10 12 or 15")
person=input("How many people to split the bill")
total_bill=(float(bill)*float(tip))/100+float(bill)
each_bill=round((total_bill/int(person)),2)
each_bill="{:.2f}".format(each_bill)
print(f"Each person should pay {each_bill}")

