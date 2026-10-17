#Q49
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%j==0:
#             print(j,end=" ")
#     print()    

#Q50
# n=int(input("Enter a Number:"))
# for i in range(1,n+1):
#     div_sum=0
#     for j in range(1,(i//2)+1):
#         if i%j==0:
#             div_sum+=j
#     if div_sum==i:
#         print(i)

#Q51
# p=int(input("Prime Number upto N:"))
# for i in range(2,p+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")

#Q52
# p=int(input("Prime Number upto N:"))
# for i in range(2,p+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(f"{i}=>1,{i};",end="  ")

#Q53
# f=int(input("Enter First Number:"))
# s=int(input("Enter Second Number:"))
# for i in range(1,f+1):
#     if f%i==0:
#         for j in range(1,s+1):
#             if s%j==0 and i==j:
#                 print(i,end=" ")

#Q54
# f=int(input("Enter First Number:"))
# s=int(input("Enter Second Number:"))
# limit=int(input("Enter a Limit Number for both Multiples:"))

# for i in range(1,f+1):
#     a=f*i
#     if a>=30:
#         break
#     for j in range(1,s+1):
#         b=s*j 
#         if a==b:
#             print(f"No Common Multiple below {limit} except {a}") 

#Q55







        



#Q53
       


