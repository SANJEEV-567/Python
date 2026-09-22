
for i in range(5):
    print("*",end="")

# Both are same Question With Nested and Without nested Loop
for row in range(4):
    for column in range(4):
        print("*", end="")
    print()

for row in range(4):
    print("*"*4)

# Both are same Question With Nested and Without nested Loop
for row in range(0,5):
    for column in range(0,row+1):
        print("*", end="")
    print() 

for i in range(5):
    print("*"*i)    

# Next Ques
for row in range(4,0,-1):
    for column in range(0,row):
        print("*", end="")
    print()

# Next Ques
for row in range(1,6):
    for column in range (1,row+1):
        print(column,end="")
    print()    

#Ques
for row in range(1,6):
    for column in range(5-row):
        print(" ", end="")
    for column in range(1,row+1):
        print("*",end="")
    print()    

#by taking input
num=int(input("Enter Row and Column Value:"))
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(1,i+1):    
        print("*",end="") 
    print()        

#Ques
num=int(input("Enter Row and Column Value:"))
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(1,i+1):    
        print("*",end="") 
    print() 