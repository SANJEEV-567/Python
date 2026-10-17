#Q11
# row=int(input("Enter a Row Number:"))
# col=int(input("Enter a Column Number:")) 
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         if j%2==0:
#             print(j,end=" ")
#     print()  

#Q12
# grid=int(input("Enter a NxN Grid Number:"))

# for i in range(1,grid+1):
#     for j in range(1,grid+1):
#         if j%2!=0:
#             print(j,end=" ")
#     print()    

#Q13
for i in range(1,5):
    for j in range(1,5):
        if (i+j)%2==0:
            print("E",end="")
        else:
            print("O",end="")
    print()            

#Q14
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")  
#     print()     

#Q15
# grid=int(input("Enter a NxN Grid Number:"))
# for i in range(1,grid+1):
#     for j in range(1,grid+1):
#         if i==j:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()    

#Q16
# for i in range(1,6):
#     for j in range(1,6):
#         if i%j==0:
#             print("X",end=" ")
#         else:
#             print("-",end=" ") 
#     print()           

#Q17
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j%i==0:
#             print(j,end=" ")
#     print()        

#Q18
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j>n:
#             print(i,j) 

#Q19
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1): 
#         if (i*j)%2==0:
#             print(f"{i} {j}",i*j)    

#Q20
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("Special",end=" ")
#         elif i+j==n:
#             print("PAIR",end=" ")
#         else:
#             print("NORMAL",end=" ")
#     print()

