#09_problem_solving
#Q1
# integer= int(input("Check type of Integer: "))
# if integer > 0:
#     print("Positive")
# elif integer <0:
#     print("Negative")
# elif integer ==0:
#     print("Zero")

#Q2
# integer= int(input("Check Positive or Negative and Even or Odd: "))
# if integer > 0 and integer%2==0:
#     print("Positive Even")
# elif integer >0 and integer%2!=0:
#     print("Positive Odd")
# elif integer<0 and integer%2==0:
#     print("Negative Even")
# elif integer<0 and integer%2!=0:
#     print("Negative Odd")
# elif integer ==0:
#     print("Zero")    

#Q3
# first_number= int(input("Enter First Number: "))
# second_number= int(input("Enter Second Number: "))
# if first_number > second_number:
#     print("First Number is Greater Than Second Number")
# elif second_number > first_number:
#     print("Second Number is Greater Than First Number")    
# elif first_number == second_number :
#     print("Both Are Equal Numbers")   
 
#Q4
# first_number= int(input("Enter First Number: "))
# second_number= int(input("Enter Second Number: "))
# third_number= int(input("Enter Third Number: "))
# if first_number > second_number > third_number:
#     print("Third is Smallest")
# elif third_number > second_number > first_number:
#     print("First Number is Smallest")
# elif first_number > third_number > second_number:
#     print("Second Number is Smallest")
# elif first_number == second_number == third_number:
#     print("All are Equal Numbers")           

#Q5
# first_number= int(input("Enter First Number: "))
# second_number= int(input("Enter Second Number: "))
# third_number= int(input("Enter Third Number: "))
# if first_number > second_number > third_number:
#     print("First Number is Largest")
# elif second_number > first_number > third_number:
#     print("Second Number is Largest")
# elif third_number > second_number > first_number:
#     print("Third Number is Largest")
# elif first_number == second_number == third_number:
#     print("All are Equal Numbers")

#Q6 Divisible by 5 and 11
# number= int(input("Check Divisiblity of 5 and 11, only 5, only11: ")
# if number%55 == 0:
#     print("Divisible by both 5 and 11")
# elif number%5 == 0:
#     print("Divisible only by 5")
# elif number%11 ==0:
#     print("Divisible only by 11") 
# else:
#     print("Divisible by neither")        

#Q7 Divisible by Either 3 or 7
# number= int(input("Check Divisiblity of 3and7, only by 3, only by 7: "))
# if number%3 == 0:
#     print("Divisible by both 3 and 17")
# elif number%7 == 0:
#     print("Divisible only by 3")
# elif number%21 ==0:
#     print("Divisible only by 7") 
# else:
#     print("Divisible by neither")

# #Q8 Pass or Fail
# marks= int(input("Check Your Result (Pass/Fail): "))
# if marks < 0:
#     print("Invalid marks")
# elif marks > 100:
#     print("Invalid marks") 
# elif marks >= 40:
#     print("Pass")
# elif marks <40:
#     print("Fail") 
          
#Q9 Grade Calculator
# grade= int(input("Check Your Grade: "))
# if grade < 0:
#     print("Invalid marks")
# elif grade > 100:
#     print("Invalid marks")
# elif 90<=grade>=100:
#     print("Grade A")
# elif 80<=grade>=89:
#     print("Grade B")
# elif 70<=grade>=79:
#     print("Grade C")
# elif 60<=grade>=69:
#     print("Grade D")            
# elif 40<=grade>=59:
#     print("Grade E")
# elif grade < 40:
#     print("Grade Fail")

#Q10
# age= int(input("Check Voting Eligibility: "))
# if age < 0:
#     print("Invalid Age")
# elif age > 120:
#     print("Rejected")    
# elif age < 18:
#     print("Cannot vote")
# elif age >=18:
#     print("Can vote")

#Q11  Leap Year
# year= int(input("Check Whether it is Leap Year or Not: "))
# if year%400:
#     print("It is a Leap Year")
# else:
#     print("Not a Leap Year")  
   
#Q12  Character Type
# character= input("Determine the type of Character(a Letter): ")
# if "A"<=character<="Z":
#     print("its a Uppercase alphabet")
# elif "a"<=character<="z":
#     print("its a Lowercase alphabet")
# elif "0"<character<"9" :
#     print("its a Digit")
# else:
#     print("its a Special Character")          

#Q13 Vowel or Consonant
# char= input("Check Whether it is Vowel or Consonant: ").lower()
# if char in ('a','e','i','o','u'):
#     print("its a Vowel")
# elif "a"<=char<="z" and char!=('a','e','i','o','u'):
#     print("its a Consonant")  
# else:
#     print("Invalid Input")    

#Q14 Profit or Loss
# cp= float(input("Enter Cost Price: "))
# sp= float(input("Enter Selling Price: "))
# if cp>sp:
#     print("Loss")
# elif sp>cp:
#     print("Profit")
# elif sp==cp:
#     print("No Profit No Loss")     
# else:
#     print("Invalid")       

#Q15 Profit/Loss Percentage
# cost_price = float(input("Enter Cost Price: "))
# selling_price = float(input("Enter Selling Price: "))
# if cost_price <= 0:
#     print("Invalid Cost Price")
# else:
#     if selling_price > cost_price:
#         profit = selling_price - cost_price
#         profit_percentage = (profit / cost_price) * 100
#         print("Profit:", profit)
#         print("Profit Percentage:", profit_percentage, "%")
#     elif cost_price > selling_price:
#         loss = cost_price - selling_price
#         loss_percentage = (loss / cost_price) * 100
#         print("Loss:", loss)
#         print("Loss Percentage:", loss_percentage, "%")
#     else:
#         print("No Profit No Loss.")

#Q16
# units = float(input("Enter the total units consumed: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# print("Total Electricity Bill: ", bill)

#Q17
# operation = int(input("Enter a number of Following operation you want to perform: \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division : "))

# if operation==1 or operation==2 or operation==3 or operation==4:

#     first_number= int(input("Enter first number: "))
#     second_number= int(input("Enter second number: "))

#     if operation==1:
#         print(f"Addition is: {first_number+second_number}")
#     elif operation==2:
#         print(f"Substraction is: {first_number-second_number}")
#     elif operation==3:
#         print(f"multiplication is: {first_number*second_number}")
#     elif operation==4:
#         print(f"Division is: {first_number/second_number}")
#     elif operation==5:
#         print(f"floor division is: {first_number//second_number}")
# else:
#     print("your opration is invalid")

#Q18 Temperature Classifier
# temperature = float(input("Enter the temperature in Celsius: "))
# if temperature < 0:
#     print("Freezing")
# elif temperature <= 15:
#     print("Very Cold")
# elif temperature <= 25:
#     print("Cold")
# elif temperature <= 35:
#     print("Normal")
# else:
#     print("Hot")

#Q19 Number Range Checker
# num = float(input("Enter a number: "))
# if num < 0:
#     print("Negative")
# elif num <= 10:
#     print("0-10")
# elif num <= 50:
#     print("11-50")
# elif num <= 100:
#     print("51-100")
# else:
#     print("Above 100")

#Q20
# a = float(input("Enter the length of side a: "))
# b = float(input("Enter the length of side b: "))
# c = float(input("Enter the length of side c: "))
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("The three sides can form a triangle.")
# else:
#     print("The three sides cannot form a triangle.")

#Q21
# a= int(input("Enter Side a: "))
# b= int(input("Enter Side b: "))
# c= int(input("Enter Side c: "))
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("Triangle is Valid.")
#     if a==b==c:
#         print("Triangle is Equilateral")
#     elif a==b!=c or a==c!=b or a!=b==c:
#         print("Triangle is Isosceles")
#     else:
#         print("Triangle is Scalene")   
# else:
#     print("Invalid Sides!!!")

#Q22
# account_balance= int(input("Enter Your Account Balance: "))
# withdrawal_amount= int(input("Withdraw Your Amount: "))    
# if withdrawal_amount > 0:
#     if withdrawal_amount%100==0:
#         if withdrawal_amount < account_balance:
#             if withdrawal_amount <= account_balance-500:
#                 print("Withdrawal Successful")
#                 if account_balance-withdrawal_amount:
#                     print(f"Remaining balance: {account_balance-withdrawal_amount}")
#                 else:
#                     print("At least Rs.500 Must Remain")
#         else:           
#             print("Insufficient Balance!!!")      
#     else:
#         print("Take a Amount Which is Divisible by 100.") 
# else:
#     print("Invalid Amount!!!")        

#Q23
# username= input("Enter Your Username: ")
# password= input("Enter Your Password: ")
# if username=="admin":
#     if password=="python123":
#         print("Login Successful")
#     else:
#         print("Wrong Password!!!")
# else:
#     print("User not found!!!")                

#Q24
original_amount = float(input("Enter purchase amount: "))

if original_amount < 500:
    discount_percentage = 0
elif original_amount <= 999:
    discount_percentage = 5
elif original_amount <= 1999:
    discount_percentage = 10
elif original_amount <= 4999:
    discount_percentage = 15
else:
    discount_percentage = 20

discount_amount = original_amount * (discount_percentage / 100)
final_amount = original_amount - discount_amount

print(f"Original amount: Rs.{original_amount}")
print(f"Discount percentage: Rs.{discount_percentage}%")
print(f"Discount amount: Rs.{discount_amount}")
print(f"Final amount: Rs.{final_amount}")

#Q25
sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
    print("Invalid input! Marks must be between 0 and 100.")

elif sub1 < 35 or sub2 < 35 or sub3 < 35:
    print("Result: Fail")

else:
    average = (sub1 + sub2 + sub3) / 3
    print("Average Marks:", average)
    
    if average >= 75:
        print("Grade: Distinction")
    elif average >= 60:
        print("Grade: First Class")
    elif average >= 50:
        print("Grade: Second Class")
    else:
        print("Grade: Pass")






















    







            

