#Q2
fail_count=pass_count=good_count=excellent_count=0
for m in range(10):
    marks=int(input("Enter Your Marks:"))
    if marks<35:
        print("Fail")
        fail_count+=1  
    elif 35<=marks<=49:
        print("Pass")
        pass_count+=1
    elif 50<=marks<=74:
        print("Good")
        good_count+=1
    elif 75<=marks<100:
        print("Excellent")
        excellent_count+=1
    else:
        print("Invalid Marks!!!")

print("No of Students fail:",fail_count)
print("No of Students Pass:",pass_count)
print("No of Students Good:",good_count)
print("No of Students Excellent:",excellent_count)





