#Q1
string= input("Enter a Character Containing Letters,digits,Spaces,Special Characters:")
upper=lower=digit=special=0

for char in string:
    if "A"<=char<="Z":
        upper+=1
    elif "a"<=char<="z":
        lower+=1
    elif "0"<=char<="9":
        digit+=1
    else:
        special+=1
print("No. of Uppercase:",upper)
print("No. of Lowercase:",lower)
print("No. of Digits:",digit)
print("No. of Special characters:",special)

if upper> lower and digit and special:
    print("Uppercase is Highest")
elif lower> upper and digit and special:
    print("Lowercase is Highest")
elif digit> upper and lower and special:
    print("Digit is Highest")
elif special> upper and lower and digit:
    print("Special characters is Highest")
elif upper == lower or digit or special:
    print("Tie")    



