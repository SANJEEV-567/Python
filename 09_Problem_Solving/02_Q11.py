#Q11
for i in range(5):
    user = input("Enter Your Username: ")
    countdigit=0
    count_un=0
    print("Length of Character:",len(user))
    print("First Character:",user[0:1])
    for j in user:
        if user== "0123456789":
            countdigit+=1
            print("No of Digit:",countdigit)
        if user=="_":
            print("No of Undersore:",count_un)  
    

