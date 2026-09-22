
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(0,2*i-1):    
        print("*",end="")
    print()  

# Ques no 8 from Class test on 12/09/2026
#Q8
total = 0
passed = True

for i in range(5):
    marks =int(input("Enter Your Marks:"))
    total = total + marks

    if marks < 35:
        passed = False

percentage = total / 5

if passed:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    print(total,percentage,grade)

if passed:
    print("You Have apassed")
else:
    print("You Have Failed!!!")  

#Q9

      




