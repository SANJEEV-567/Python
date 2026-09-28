# Question 15
#Math Based Logic
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(i)
# even=n//2
# print(f"No. of even number are:{even}")

# #Py Logic
# word = "Python"
# count = 0
# for character in word:
#     count = count + 1
# print("Characters:", count)

#while
n=int(input("Enter a Number:"))
i=1
count=0
while i<=n:
    if i%2==0:
        count+=1
    i+=1
print("No. of Even Numbers upto n:",count,end="")   
   
