#Q4
for pwd in range(5):
    password=input("Enter Your password:")

    has_len= len(password)>=8
    has_upper=False 
    has_lower=False
    has_digit=False
    has_special=False

    for char in password:
        if "A"<=char<="Z":
            has_upper=True
        elif "a"<=char<="z":
            has_lower=True
        elif "0"<=char<="9":
            has_digit=True
        else:
            has_special=True

    score=0
    if has_len:
        score+=1
    if has_upper:
        score+=1
    if has_lower:
        score+=1
    if has_digit:
        score+=1
    if has_special:
        score+=1

    if score==5:
        print('Your Password is Strong')
    elif score==3 or score==4:
        print("Your password is Medium")
    elif score<3:
        print("Your Password is Weak") 
              


