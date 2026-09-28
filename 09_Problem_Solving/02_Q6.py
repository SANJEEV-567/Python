#Q6
for n in range(5):
    num=input("Enter a Numbers:")
    even=0
    odd=0

    for d in num:
        digit=int(d)
        if digit%2 == 0:
            even+=1
        else:
            odd+=1

    if even>odd:
        print("More Even Digits")            
    elif odd>even:
        print("More Odd Digits")
    else:
        print("Both Even Digit and Odd Digit are Equal")    




