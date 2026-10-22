#Q57
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()    

#Q58
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()   

#Q59
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print() 

#Q60
# n=int(input("Enter a Row Number:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()    

#Q61
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()    

#Q62
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print()  

#Q63
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(i,end="")
#     print()

#Q64
# n=int(input("Enter a Row Number:"))
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(i,end="")
#     print()

#Q65
# n=int(input("Enter a Row Number:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()

#Q66
# r=int(input("Enter a Row Number:"))
# c=int(input("Enter a Column Number:"))
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         if i==1 or i==r or j==1 or j==c:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

#Q67
# t=int(input("Enter a Number:"))
# for i in range(1,t+1):
#     for j in range(1,i+1):
#         if j==1 or i==t or i==j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()      

#Q68
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("1",end="")
#         else:
#             print("0",end="")
#     print()     

#Q69
# n=int(input("Enter a Number:"))
# for i in range(n):
#     for j in range(n):
#         if (i==j or j== n-i-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()     
