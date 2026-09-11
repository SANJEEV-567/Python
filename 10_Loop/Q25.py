# Question 25
# method 1
text = input("Enter a string: ")
count = 0
for char in text:
    if char.isupper():
        count += 1
print("Number of uppercase characters:", count)

#method2
text = input("Enter a string: ")
count = 0
for char in text:
    if "A"<=char<="Z":
        count += 1
print("Number of uppercase characters:", count)
