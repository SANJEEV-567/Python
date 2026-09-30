# Question 18
# n= int(input("Enter a Number:"))
# total = 0
# for i in range(1,n + 1 ,2):
#     total = total + i
# print(total)

#Q18
n= int(input("Enter a Number:"))
i=1
sum=0

while i<n:
    
    i+=2
    sum+=i
print("total sum of Even numbers:",sum,end="")