#Q1
# marks=int(input("Enter Your marks(0-100):"))
# while marks:
#     if 0<=marks<=100:
#         print(marks)
#         break
#     else:
#         print("Invalid Marks!")
#         marks=int(input("Enter Your marks(0-100):"))

#Q2
# num=int(input("Enter a Number:"))
# while num:
#     if num>0:
#         print(num)
#         break
#     else:
#         print("Not a Positive Number")
#         num=int(input("Enter a Number:"))   

#Q3
# age=int(input("Enter Your Age(0-120):"))
# while age:
#     if 0<=age<=120:
#         print(age)
#         break
#     else:
#         print("Invalid Age!")
#         age=int(input("Enter Your Age(0-120):"))

# #Q4
# menu=int(input("Select a Valid Choice\n1. View profile\n2. Edit profile\n3. Settings\n4. Exit :"))
# while menu>=1:
#     if menu<=4:
#         print(menu)
#         break
#     else:
#         print("Invalid Choice!")
#         menu=int(input("Select a Valid Choice\n1. View profile\n2. Edit profile\n3. Settings\n4. Exit :"))

#Q5
# password=input("Enter Your password(min 8 characters):").strip()
# while password:
#     if len(password)>=8:
#         print("You Have Logged in")
#         break
#     else:
#         print("Invalid password!")    
#         password=input("Enter Your password(min 8 characters):").strip()

#Q6 #Without if condition (Krish Method)
# temp=int(input("Enter a Temperature(-20 between 45):"))
# while temp<-20 or temp>45:
#     temp=int(input("Enter a Temperature(-20 between 45):"))
      
# print(temp)

#Q7
# balance=5000
# while balance:
#     withdrawal=int(input("Enter Withdrawal Amount:"))
#     if withdrawal<=0:
#         print("Try Again!")
#     elif withdrawal>balance:
#         print("Insufficient Balance!")   
#     else:
#         balance-=withdrawal
#         print("Remaining Balance:",balance)    
#         break

#Q8
# username=input("Enter Your Username:").strip()
# while len(username)<5 or " " in username:
#     username=input("Enter Your Username:").strip()
# print(username)    


#Q9
# n=int(input("Enter a Positive Integer Divisible by 3 and 5:"))
# while n>0:
#     if n%3==0 and n%5==0:
#         print(n)
#         break
#     else:
#         print("Rejected, The Number is Not Divisble by Both 3 and 5.")
#         n=int(input("Enter a Positive Integer Divisible by 3 and 5:"))

#Q10
# for i in range(3):
#     pin=int(input("Enter Your Privacy Pin:"))
#     if pin==2468:
#         print("Login Successful")
#         break
# else:
#     print("Access Denied!") 

#Q11 Without break 
# integer=int(input("Enter a Number 10 and 50:"))
# while integer<10 or integer>50:
#     integer=int(input("Enter a Number 10 and 50:"))
# if integer%2==0:
#     print("Even")    
# else:
#     print("Odd")    

#Q12
#Method 1
# balance=2000
# deposit=float(input("Enter the Amount You Want Deposit:"))
# while deposit>0:
#     balance+=deposit
#     print("Your New balance is:",balance)
#     break

#Method 2 (More Accurate according to question)
# balance=2000
# deposit=float(input("Enter the Amount You Want Deposit:"))
# while deposit<=0:
#     deposit=float(input("Enter the Amount You Want Deposit:"))
# balance+=deposit
# print("New balance:",balance)

#Q13
# num=int(input("Enter a Number(1-100):"))
# while num<1 or num>100:
#     num=int(input("Enter a Number(1-100):"))
# print(num)

#Q14
# marks=int(input("Enter Your Marks(0-100):"))   
# while marks<0 or marks>100:
#     marks=int(input("Enter Your Marks(0-100):")) 
# if marks>=75:
#     print("Distinction") 
# elif marks>=60:
#     print("First Class")
# elif marks>=35:
#     print("Pass")
# else:
#     print("Fail")    

#Q15
# user=input("Enter Your Username:").strip()
# password=input("Enter Your Password:").strip()         

# while len(user)<5 or " " in user or len(password)<8 or " " in password:
#     user=input("Enter Your Username:").strip()
#     password=input("Enter Your Password:").strip()         
# print("You Have Logged in")     

#Q16
# first=int(input("Enter First Number:"))
# second=int(input("Enter Your Second Number:"))
# operator=int(input("Select a Operator You Want to Perform\n1.Add\n2.Subtract\n3.Multiply\n4.Divide :"))

# while operator<1 or operator>4:
#     first=int(input("Enter First Number:"))
#     second=int(input("Enter Your Second Number:"))
#     operator=int(input("Select a Operator You Want to Perform\n1.Add\n2.Subtract\n3.Multiply\n4.Divide :"))

# if operator==1:
#     add=first+second
#     print("Addition:",add)
# elif operator==2:
#     sub=first-second
#     print("Substraction:",sub) 
# elif operator==3:
#     mul=first*second
#     print("Multiplication:",mul) 
# elif operator==4 and second!=0:
#     divide=first/second
#     print("Division:",divide) 
# else:
#     print("Division by Zero is Not Possible!")             
#     second=int(input("Enter Your Second Number:"))
#     divide=first/second
#     print("Division:",divide)

#Q17
# balance=10000
# option=int(input("Select a banking option\n1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit : "))

# while option<1 or option>4:
#     deposit=float(input("Enter the Amount You Want Deposit:"))
#     withdrawal=int(input("Enter Withdrawal Amount:"))

#Q18
# month=int(input("Enter a Month Number:"))
# day=int(input("Enter a Date:"))

# while month<1 or month>12 or day<1 or day>31:
#     month=int(input("Enter a Month Number:"))
#     day=int(input("Enter a Date:"))

#Q19
# quantity=int(input("Enter Product Quantitiy:"))
# unit_price=int(input("Enter a Product Price:"))

# while quantity<1 or unit_price<1:
#     quantity=int(input("Enter Product Quantitiy:"))
#     unit_price=int(input("Enter a Product Price:"))
# print("Total Cost:",quantity*unit_price)    

#Q20

#Q21
# password=input("Enter a Strong Password:").strip()
# has_upper=False     
# has_lower=False
# has_digit=False
    
# while len(password)>=8:
#     if "A"<=password<="Z":
#         has_upper=True
#     if "a"<=password<="z":
#         has_lower=True
#     if "0"<=password<="9":
#         has_digit=True
#     else:
#         print("Invalid password!")
#         password=input("Enter a Strong Password:").strip()

#Q22

#Q23
score1=int(input("Enter Your First Score(0-100):"))
score2=int(input("Enter Your  Second Score(0-100):"))
score3=int(input("Enter Your Third Score(0-100):"))

while score1<0 or score1>100:
    score1=int(input("Enter Your First Score(0-100):"))
    while score2<0 or score2>100:
        score2=int(input("Enter Your Second Score(0-100):"))
        while score3<0 or score3>100:
            score3=int(input("Enter Your Third Score(0-100):"))

total=score1+score2+score3
avg=total/3
print("Total Score:",total)
print("Average Score:",avg)


#Q24
# balance=10000
# withdrawal=int(input("Enter Withdrawal Amount:"))

# while withdrawal<1 or balance<withdrawal or withdrawal%100!=0:
#     withdrawal=int(input("Enter Withdrawal Amount:"))
# balance-=withdrawal
# print("Withdrawal Amount:",withdrawal)
# print("Remaining Balance:",balance)

    

    
























