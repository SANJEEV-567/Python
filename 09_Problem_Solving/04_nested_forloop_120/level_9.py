#Q70
# n=int(input("Enter a Number:"))
# word=input("Enter a Character:").upper()
# for i in word:
#     for j in range(1,n+1):
#         print(f"{i}{j}",end=' ')
#     print()    

#Q71
# c=input("Enter a Character:").upper()
# for i in range(len(c)):
#     for j in range(i+1,len(c)):
#         if j-i>5:
#             print(c[i],c[j])

#Q72 ##########

#Q73
# def reportCard(m1,m2,m3,m4):
#     total=m1+m2+m3+m4
#     avg=total/4
#     result=f"Student total Marks:{total} and Averages:{avg}."
#     return result

# by Nested for loop
# total=0
# for s in range(3):
#     student=input("Enter Your Name:").title()
#     for m in range(4):
#         marks=int(input("Enter Your Marks:"))
#         total+=marks
#         avg=total/4
#     print(f"{student} totals:{total}  and average:{avg}")

#Q74
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()    

#Q75
# s=int(input("No. of Student:"))
# p=0
# a=0
# for i in range(1,s+1):
#     name=input("Enter Your Name:").title()
#     days=int(input("Enter No. of Days Attendance You Want to Check:"))
#     for j in range(1,days+1):
#         attendance=input("Mark Your Attendance:").upper().strip()
#         if attendance=="P":
#             p+=1
#         elif attendance=="A":
#             a+=1
#         else:
#             print("Invalid Input!!!")
#     print(f"{name}: Present={p} Absent={a}")                

#Q76
# r=int(input("Enter a Row Number:"))
# c=int(input("Enter a Column Number:"))
# a=65
# for row in range(r):
#     for col in range(1,c+1):
#         print(f"{chr(a)}{col}",end=" ")
#     a+=1    
#     print()    

#Q77
# r=int(input("Enter a Row Number:"))
# s=int(input("Enter No. of Seats in a Row:"))
# for i in range(1,r+1):
#     for j in range(1,s+1):
#         if j%2==0:
#             print("150",end=" ")
#         else:
#             print("100",end=" ")    
#     print()

#Q78
# s=int(input("No. of Student:"))
# p=0
# a=0
# for i in range(1,s+1):
#     name=input("Enter Your Name:").title()
#     days=int(input("Enter No. of Days Attendance You Want to Check:"))
#     for j in range(1,days+1):
#         attendance=input("Mark Your Attendance:").upper().strip()
#         if attendance=="P":
#             p+=1
#         elif attendance=="A":
#             a+=1
#         else:
#             print("Invalid Input!!!")
           