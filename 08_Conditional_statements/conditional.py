
#Q1
number= 11
if number > 10:
    print("Greater than 10")

#Q2
age = 20
if age >= 18:
    print("Adult")

#Q3
# number= input("Enter a Integer: ")
# if age > 0:
    # print("Positive")

#Q4
marks= 75
if marks >= 45:
    print("Pass")

#Q5
# number= int(input("Enter a Number: "))
# if number == 0:
    # print("Zero")

#Q6
# integer= int(input("Write a Interger: "))
# if integer >= 0:
#     print("Positive")
# else:
#     print("Not Positive")

#Q7
# age = 16

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

#Q8
# number= input("Check Here Even , Odd: ")
# if number==0:
#     print("Even")
# else:
#     print("Odd")

#Q9
# marks= int(input("Enter Your Marks: "))
# if marks >=40:
#     print("Pass")
# else:
#     print("Fail")

#Q10
#Python provides elif, which means: Check another condition if the previous condition was False.
# marks = int(input("Check Ypur Grade: "))
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")    
# elif marks >= 60:
#     print("c")
# elif marks >= 40:
#     print("D")
# elif marks <40:
#     print("F")    

#Q12
# number= int(input("check number type: "))
# if number > 0:
#     print("Positive")
# elif number == 0:
#     print("Zero")
# else:
#     print("Negative")

# #Q13
# number = int(input("Enter Day Index: "))

# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number== 5:
#     print("Friday")    

#Q14
marks = 75
if marks >= 90:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#Q15
# number= int(input("take a number: "))
# if number ==1:
#     print("1")
# elif marks ==2:
#     print("2")
# elif marks ==3:
#     print("3")
# else:
#     print("Other")

#Nested conditions
#Q16
age = 20
if age >= 18:
    if age <= 60:
        print("Between 18 and 60")

################Q17
# Take marks from the user
# marks = float(input("Enter the student's marks: "))

# First check whether the student passed (marks >= 40)
# if marks >= 40:
#     # If the student passed, check whether marks are at least 75
#     if marks >= 75:
#         print("Good")
#     else:
#         print("Passed")
# else:
#     # If the student did not pass
#     print("Failed")

#Q18
# integers= int(input("enter a interger: "))
# if integers >= 0:
    # if integers > 100:
        # print("Greater than 100")
    # else:
        # print("Positive")
# else:
    # print("Negative")         

#Q19
age = 20

if age >= 18:
    if age <= 60:
        print("Age is between 18 and 60")
else:
    print("Your are Minor")

#Q20
# number= int(input("Enter a number: "))

# if number != 0:
#     if number >= 0:
#         print("Positive")
#     else:
#         print("Negative")    
# else:
#     print("Zero")        

#Q21
# age= int(input("Enter your Age: "))
# marks= int(input("Enter your Marks: "))
# if age >= 18 and marks >= 40:
#     print("Eligible")   

#Q22
# number= int(input("Enter a Number: "))
# if number < 10 or number > 100 :
    # print("Special")

#Q23
your_age= int(input("your age: "))
has_id= input("Do you Have id(yes/no): ")    
if age >= 18 and has_id=="yes" :
    print("Allowed")
else:
    print("Not Allowed!!!")

#Q24
# first_number= int(input("Enter first number: "))
# second_number= int(input("Enter second number: "))
# if first_number > 10 and second_number > 10:
    # print("Both are greater than 10")

#Q25
# number= int(input("Enter a number: "))
# if number < 0 or number> 100:
    # print("Allowed")

#Q26
# is_closed = False
# if not is_closed:
#     print("open")

#Q27
# number= int(input("Enter a Number: "))
# if number > 10 and number < 50:
    # print("between 10 and 50")
# else:
    # print("not in between 10 and 50")

#Q28    
# number= int(input("Enter a Number: "))
# if number > 10 or number < 50:
    # print("between 10 and 50")

#Q29
is_student = input("Are you a Student(Yes/No): ")
has_id= input("Do you have id (Yes/No):  ")
has_ticket = input("Do you Have Ticket(Yes/No): ")

if is_student=="yes" and has_id=="yes" and has_ticket=="yes":
    print("Allowed")
else:
    print("Invalid!!!")

#Q30
age= int(input("Enter Your Age: "))
marks= int(input("Enter your marks: "))
has_id= input("Do you have id (Yes/No):  ")
if age >= 18 and marks >= 40 and has_id== "yes":
    print("Eligible")
elif has_id== "no":
    print("You Do not Have Valid id!!!")    
else:
    print("Not Eligible")