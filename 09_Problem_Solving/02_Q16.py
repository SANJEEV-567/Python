#Q16
password=(input("Enter Your Password:"))
upper=lower=digit=special=0

for char in password:
    if "A" <=password>="Z":
        upper+=1
    elif "a"<=password>="z":
        lower+=1
    elif "0"<=password>="9":
        digit+=1
    else:
        special+=1

    print("Percentage of Uppercase:",upper/len(char))                
    print("Percentage of Lowercase:",lower/len(char))                
    print("Percentage of Digits:",digit/len(char))                
    print("Percentage of Special Characters:",special/len(char))  
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
    