#Q21
# char=input("Enter a Word:").upper()
# for i in char:
#     for j in range(1,4):
#         print(i,end="")
#     print()    

# Q22 Character with Position
# cp=input("Enter Character:").upper()
# for i in cp:
#     for j in range(3):
#         print(i,j)

#Q23
# s=input("Enter Character:").upper()
# for i in s:
#     for j in s:
#         if i==j:
#             print(f'{i}/{j} is Same;',end=" ")
#         else:
#             print(f"{i}/{j} is Different.",end=" ") 
              
#Q24
# s1=input("Enter first str:").upper()
# s2=input("Enter second str:").upper()
# for i in s1:
#     for j in s2:
#         if i==j:
#             print(i,j) 

#Q25
# s1=input("Enter first str:").upper()
# s2=input("Enter second str:").upper()
# count=0
# for i in s1:
#     for j in s2:
#         if i==j:
#             count+=1
# print(count) 

#Q26 ###############################
char="banana".upper()
count=0
for i in char:
    for j in char:
        if i==j:
            count+=1  
    else:
        print(f"{i} = {count}")    


#Q27
# vcc=input("Enter a Character or Word:").strip()
# vowel="AEIOUaeiou"
# for i in vcc:
#     for j in vowel:
#         if i==j:
#             print(i,"=","Vowel")    
#             break
#     else:
#         print(i,"=","Consonant")
               

# #Q28
# s1=input("Enter first str:").upper()
# s2=input("Enter second str:").upper() 
# for i in s1:
#     for j in s2: 
#         if i==j:
#             print(f"Common characters include {j}")
 
#Q29
# s1=input("Enter Characters:").upper() 
# for i in s1:
#     for j in s1:
#         print(i,j)

#Q30
# s1=input("Enter Characters:").upper() 
# for i in s1:
#     for j in s1:
#         if i!=j:
#             print(i,j,end=",")