# # Q1: Define a function named welcome that prints Welcome to Python. Call it three times.
# def welcome():
#     print("Welcome to Python")

# welcome()
# welcome()
# welcome()


# # Q2: Define greet(name) that prints a greeting using the given name.
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Sanjeev")


# # Q3: Define show_number(number) that prints the number passed to it.
# def show_number(number):
#     print(number)

# show_number(10)


# # Q4: Define add(a, b) that returns the sum of two numbers.
# def add(a, b):
#     return a + b

# sum_result = add(5, 7)
# print("Sum:", sum_result)


# # Q5: Define square(number) that returns the square of a number.
# def square(number):
#     return number ** 2

# print("Square:", square(4))


# # Q6: Define is_even(number) that returns True if the number is even and False otherwise.
# def is_even(number):
#     return number % 2 == 0

# print("Is 4 even?", is_even(4))
# print("Is 7 even?", is_even(7))


# # Q7: Define get_full_name(first_name, last_name) that returns the full name.
# def get_full_name(first_name, last_name):
#     return f"{first_name} {last_name}"

# full_name = get_full_name("Sanjeev", "Kumar")
# print("Full Name:", full_name)


# # Q8: Define introduce(name, city="Pune") and test it with and without a city argument.
# def introduce(name, city="Pune"):
#     print(f"My name is {name} and I live in {city}.")

# introduce("Sanjeev")

# introduce("Abhishek", "Mumbai")


# # Q9: Define subtract(a, b) and show how changing positional argument order changes the result.
# def subtract(a, b):
#     return a - b

# result1 = subtract(10, 4)
# print("subtract(10, 4) =", result1)

# result2 = subtract(4, 10)
# print("subtract(4, 10) =", result2)


# # Q10: Define get_min_max(a, b) that returns both the smaller and larger values
# def get_min_max(a, b):
#     if a < b:
#         return a, b
#     else:
#         return b, a

# smaller, larger = get_min_max(25, 10)
# print("Smaller:", smaller, "| Larger:", larger)

# Q11: Define calculate(a, b) that returns the sum, difference, product, and quotient. Assume b is not zero.
def calculate(a, b):
    add = a + b
    diff = a - b
    product = a * b
    division = a / b
    return add, diff, product, division

s, d, p, q = calculate(10, 2)
print("calculate(10, 2) -> Sum:", s, "Difference:", d, "Product:", p, "Quotient:", q)


# Q12: Define count_digits(number) that returns the number of digits in a non-negative integer. For this exercise, treat 0 as having one digit.
def count_digits(number):
    return len(str(number))

print("Digits in 0:", count_digits(0))
print("Digits in 12345:", count_digits(12345))


# Q13: Define classify_number(number) that returns "Positive", "Negative", or "Zero".
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print("classify_number(15):", classify_number(15))
print("classify_number(-8):", classify_number(-8))
print("classify_number(0):", classify_number(0))


# Q14: Define calculate_total(price, quantity=1) that returns the total price.
def calculate_total(price, quantity=1):
    return price * quantity

print("total:", calculate_total(50))
print("total:", calculate_total(50, 3))


# Q15: Define create_email(username, domain="example.com") that returns an email address.
def create_email(username, domain="example.com"):
    return f"{username}@{domain}"

print("email:", create_email("sanjeev"))
print("email:", create_email("sanjeev", "gmail.com"))


# Q16: Define format_name(first, last, uppercase=False). If uppercase is True, return the full name in uppercase.
def format_name(first, last, uppercase=False):
    full_name = f"{first} {last}"
    if uppercase:
        return full_name.upper()
    return full_name

print("format_name('sanjeev', 'kumar'):", format_name("sanjeev", "kumar"))
print("format_name('sanjeev', 'kumar', uppercase=True):", format_name("sanjeev", "kumar", uppercase=True))


# Q17: Define percentage(marks, total=100) that returns the percentage. Assume total is not zero.
def percentage(marks, total=100):
    return (marks / total) * 100

print("percentage:", percentage(85))
print("percentage:", percentage(420, 500))


# Q18: Define convert_minutes(minutes, seconds_per_minute=60) that returns the total seconds.
def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute

print("convert_minutes:", convert_minutes(5))
print("convert_minutes:", convert_minutes(2, 60))


# Q19: Define student_details(name, age, city) and call it using keyword arguments in a different order.
def student_details(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

student_details(city="Pune", name="Sanjeev", age=21)


# Q20: Define bill(item, quantity=1, price=100) that returns the bill amount. Test positional and keyword calls
def bill(item, quantity=1, price=100):
    p= quantity*price
    a=(f"{item} {p}")
    return a

# Positional call
print("Bill (positional):", bill("Book", 3, 150))

# Keyword call
print("Bill (keyword):", bill(item="Pen", price=25, quantity=4))

# Default values
print("Bill (defaults):", bill("Notebook"))

#Q21: Define analyze_number(number) that returns three values: the absolute value, whether it is even, and the number of digits. Do not use abs(); assume the input is an integer.
def analyze_number(number):
    if number>=0:
        if number%2==0:
            a="Even"
            b=f"No. of digits: {len(str(number))}"
            return number,a,b
        else:
            a="Odd"
            b=f"No. of digits: {len(str(number))}"
            return number,a,b
    else:
        n=number*(-1)
        if n%2==0:
            a="Even"
            b=f"No. of digits: {len(str(n))}"
            return n,a,b
        else:
            a="Odd"
            b=f"No. of digits: {len(str(n))}"
            return n,a,b

print(analyze_number(number=int(input("Enter a Number:"))) )   #Here we can do Multiple Assignment to destructure tupple    

#Q22
def calculate_stats(a, b, c):
    sum=a+b+c
    if a>b and a>c:
        if b>c:
            return f"{c} is Smallest And {a} is Largest Number And Sum = {sum}"
        else:
            return f"{b} is Smallest And {a} is Largest Number And Sum = {sum}"
    if b>a and b>c:
        if a>c:
            return f"{c} is Smallest And {b} is Largest Number And Sum = {sum}"
        else:
            return f"{a} is Smallest And {b} is Largest Number And Sum = {sum}"    
    if c>a and c>b:
        if b>a:
            return f"{a} is Smallest And {c} is Largest Number And Sum = {sum}"
        else:
            return f"{b} is Smallest And {c} is Largest Number And Sum = {sum}" 

print(calculate_stats(10,20,30))

#Q23
def make_sentence(subject, verb, object):
    sen= f"{subject} is {verb} on {object}"
    return sen

print(make_sentence(verb="Sleeping",subject="Suman",object="Desk"))

#Q24
def apply_discount(price, discount=0): 
    discountprice=price*(discount/100)
    finalprice=price-discountprice
    return finalprice

print(apply_discount(500,10))

#Q26
def calculate_pay(hours,rate=200,bonus=0):
    return hours*rate+bonus

print(calculate_pay(6,bonus=50,rate=200))
print(calculate_pay(8,400,20))

#Q27
def compare(a,b):
    if a>b:
        g="A is greater"
        diff=a-b
    elif b>a:
        g="B is greater"
        diff=b-a
    else:
        g="Equal"
        diff=a-b
    return f"{g} and  Absolute Difference is:{diff}"           

print(compare(7,5))

#Q28
def convert_temperature(value, scale="C"):
    if scale.upper() == "C":
        return (value * 9/5) + 32  # Celsius to Fahrenheit
    elif scale.upper() == "F":
        return (value - 32) * 5/9  # Fahrenheit to Celsius

print(convert_temperature(56,"c"))

#Q29
def calculate_result(marks, passing_marks=35):
    if marks>=passing_marks:
        return "Pass"
    else:
        return "Fail"
print(calculate_result(75))    
#Q30
def order_summary(item, quantity=1, price=100, delivery_fee=40):
    totalcost=quantity*price+delivery_fee
    return f"Item Name: {item} and Total Cost: {totalcost}"

print(order_summary("Maggi",4,20,delivery_fee=60))












