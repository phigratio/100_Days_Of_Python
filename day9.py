# import math
# programming_dictionary={
# "Bug":"An error in a program that prevents the program from running as expected","Function":"A piece of code that can easily call over and over again. ","Loop":"The action of doing something over and over again.",
# }
# print(programming_dictionary["Bug"])
# programming_dictionary["Help"]="The fulfilling of need of someone"
# print(programming_dictionary)
# empty_dictionary={}
# # programming_dictionary={}
# print(programming_dictionary)
# programming_dictionary["Bug"]="A moth in your computer"
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
# student_scores={"Harry":82,"Ron":78,"Hermonie":99,"Draco":74,"Neville":62}
# student_grades={}
# for scores in student_scores:
#     score=student_scores[scores]
#     if score>90:
#         student_grades[scores]="Outstanding"
#     elif score>80:
#         student_grades[scores]="Exceeds Expectations"
#     elif score>70:
#         student_grades[scores]="Great"
#     else:
#         student_scores[scores]="fail"
# print(student_grades )
# capitals={{"cities_visited":"France":"Paris","Germany":"Berlin"}}
# travel_log={"France":["Paris","Lille","Dijon"],
#             "Germany":["Berlin","Hamburg","Stuttgart"],}
# bids={}
# bidding_finished=False
# while not bidding_finished:
#     name = input("What is your name?")
#     price = input("What is your bid? $")
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
#     if should_continue == "no":
#         bidding_finished = True
#     elif should_continue=="yes":
#         clear()
def total_sum(matrix):
    n = len(matrix)
    boundary_sum = 0
    diagonal_sum = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                boundary_sum += matrix[i][j]
            if i == j:
                diagonal_sum += matrix[i][j]
            if i + j == n-1:
                diagonal_sum += matrix[i][j]
    suma=boundary_sum + diagonal_sum-matrix[0][0]-matrix[0][n-1]-matrix[n-1][0]-matrix[n-1][n-1]
    odd=(n-1)/2
    if n%2==0:
        suma=suma
    else:
        suma-=matrix[odd][odd]
    return suma

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(total_sum(matrix))



