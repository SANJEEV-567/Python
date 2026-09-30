# Question 19
# n= int(input("Enter a Number:"))
# for i in range(1,11):
#     print(n*i)

#Q19
n= int(input("Enter a Number:"))
row=1
while row<=n:
    col=0
    while col<10:
        col+=1
        print(row*col,end=" ")
    print()
    row+=1
