# fruit=["apple","mango","peer"]
# for fol in fruit:
#     print(fol)
#     print(fol+" pie")
# student_height=input("input a list of heights").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)
# sum=0;
# for n in range(0,len(student_height)):
#     sum=sum+int(student_height[n])
# average=sum/len(student_height)
# print(f"Average student height is {average}")
# student_marks=input("Input the marks of students").split()
# student_no=0

# for n in student_marks:
#     student_no+=1
# for n in range(0,student_no):
#     student_marks[n]=int(student_marks[n])
# highest=0
# for n in range(0,student_no):
#     if(student_marks[n]>highest):
#         highest=student_marks[n]
# print(highest)
#
# if (n % 2 == 0):
#     sum += n
# print(sum)
# sum=0
# for n in range(0,101,2):
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','_']
print("Welcome to the password generator\n")
let=int(input("How many letters do u want in your password\n"))
num=int(input("How many numbers do u want in your password\n"))
sym=int(input("How many symbols do u want in your password\n"))
total=let+num+sym
password_list=[]
for n in range(0,let):
   random_letter=random.choice(letters)
   password_list.append(random_letter)
for n in range(0,num):
   random_number=random.choice(numbers)
   password_list.append(random_number)
for n in range(0,sym):
   random_sym=random.choice(symbols)
   password_list.append(random_sym)
random.shuffle(password_list)
password=""
for n in password_list:
    password+=n
print(password)
