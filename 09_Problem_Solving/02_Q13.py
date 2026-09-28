#Q13
for e in range(6):

    units=int(input("Enter Your Electricity Usage(in Units):"))
    if units<=100:
        bill=units*5
    elif 100<units<=200:
        bill= (100*5) + ((units-100)*7)
    elif 200<units<=400:
        bill=(100*5) + ((units-100)*7) +((units-200)*10)
    elif units>400:
        bill=(100*5) + ((units-100)*7) +((units-200)*10) + ((units-400)*15)
    
    print("Your total Electricity Bill is:",bill)

if bill<1000:
    print("Low")
elif 1000<=bill>=3000:
    print("Medium") 
if bill>3000:
    print("High")


