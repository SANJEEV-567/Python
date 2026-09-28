#Q8
for price in range(3):
    product_price=int(input("Enter the Product Price:"))

    budget=regular=premium=luxury=0
    total_amount=0

    if product_price<500:
        budget+=1
        total_amount+=product_price
    if 500<=product_price<=1999:
        regular+=1
        total_amount+=product_price
    if 2000<=product_price<=4999:
        premium+=1 
        total_amount+=product_price
    if product_price>=5000:
        luxury+=1
        total_amount+=product_price
total_amount+=product_price
average_price=total_amount/8

print("Total Amount: Rs.",total_amount)
print("Avg Price:Rs.",average_price)
print("Budget Items:",budget)
print("Regular Items:",regular)  
print("Premium Items:",premium)        
print("Luxury Items:",luxury) 




