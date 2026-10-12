
##Q1
# 1
# 2
# 3
# 4
# Finished

##Q2
#s
#k
#y
#l

##Q3
#2
#4
#6

#Q4
# num_limit=int(input("Enter a Limit Number:"))
# for i in range(1,num_limit+1):
#     if i==7:
#         break
#     print(i)

#Q5
# target_chr=input("Enter the Text:")
# for i in target_chr:
#     print(i,end=" ")
#     if i=="p":
#         break

#Q6
# integer=[4,8,2,-3,9]
# for i in integer:
#     if i<0:
#         break
#     print(i)

#Q7
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2
# Because inner loops is breaking not outer Loop

#Q8
# sen=input("Enter a Sentence:").lower().split()
# for i in sen:
#     if i=="java":
#         print("Found")
#         break 
# else:
#     print("Not Found")

#Q9
#1
#2
#3
#5
#6

#Q10
# dctn

#Q11
#1
#2
#4
#5

#Q12
# integer=int(input("Enter a Number:"))
# for i in range(1,integer+1):
#     if i%3==0:
#         continue
#     print(i)

#Q13
# word=input("Enter a Word:").lower().strip()
# for i in word:
#     if i=="s":
#         continue
#     print(i)

#Q14
marks=[25 ,40 ,75 ,32 ,90]
for i in marks:
    if i<40:
        continue
    print(i)

#Q15
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4

#Q16
n = 0

while n < 5:
    if n == 3:
        n+=1
        continue
    n += 1
    print(n)

#Q17
# word=input("Enter a Word:").lower().strip()
# vowel= "aeiou"
# count=0
# for i in word:
#     if i in vowel:
#         continue
#     count+=1
# print(count) 

#Q18
#1
#2
#3
#Done

#Q19
#1
#3
#4
#Completed

#Q20
#1
#2
#Outside loop

#Q21
#Else block

#Q22
integer=[4,8,12,16]
for i in integer:
    if i==12:
        print("Found")
        break
else:
    print("Not Found")

#Q23
# word=input("Enter a Word:")
# for i in word:
#     if i in "g":
#         print("Character exists")
#         break
# else:
#     print("Character missing")        

#Q24
# n=int(input("Enter A Number:"))
# for i in range(2,n):
#     if n%i==0:
#         print("Not prime")
#         break
# else:
#     print("Prime")

#Q25
# All are even

#Q26
# A
# 
# C

#Q27
fruit="banana"
count=0
for i in fruit:
    if i in "a":
        count+=1
        if count>=2:
            print("a")
            break
else:  
    print("no repeated character")          

#Q28
#1
#2
#3

#Q29
#Finished

#Q30
#Loop ended

#Q31
for i in range(1,6):
    if i%2==0:
        pass
    print(i)

#Q32
# choice = input("Enter your choice: ")

# if choice == '1':
#     print("Dosa")
# elif choice == '2':
#     pass 
# else:
#     print("Invalid choice!")

# print("Program closed")

#Q33 A
# 1
# 2
# 3
# 4

#Q33 B
# 1
# 2
# 4

#Q34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#Q35
#1
#3

#Q36
x=[-2,4,7,9]
for i in x:
    if i<0:
        continue
    if i==7:
        print("Target Found")
        break
else:
    print("Target not found")    

#Q37
n=[2,0,4,-1,8]
for i in n:
    if i==0:
        continue
    if i== -1:
        break
    print(i)
else:
    print("All values processed")

#Q38
# 1 1
# 1 3
# Inner loop completed
# 2 1
# 2 3
# Inner loop completed

#Q39
num=[-3,8,12,24]
for i in num:
    if i<0:
        continue
    if i%4==0 and i%6==0:
        print("Found:",i)
        break
else:
    print("No matching number")  

#Q40
#1. break
#2. continue
#3. for-else
#4. pass
#5. continue
#6. break
#7. for-else
#8. pass