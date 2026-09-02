text = "Python"

print(text[0])
print(text[3])
print(text[-1])
print(text[-2])

text = "Programming"

print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])

text = "Hello World"

print(len(text))
print(text[5])
print(text[-1])

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

text = "banana"

print(text.find("a"))
print(text.find("z"))
print(text.count("a"))

text = "Python"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

text = "I like Java"
print(text.replace("Java", "Python"))

text = "Hello"
print(text + " World")
print(text * 3)

#part 3 
# task 1
name = 'sanjeev'
city = "patna"
favorite_language = "Python"
message = f"Hello, my name is {name}. I live in {city} and my favorite programming language is {favorite_language}."
print(name)
print(city)
print(favorite_language)
print(message)

#task 2
text = ""
print(len(text))
print(type(text))

#task 3
text = "Python Programming"
print(text[0:18])
print(len(text))
print(text[0])
print(text[-1])
print(text[2])
print(text[-2])

#task 4
dev = "Programming"
print(dev[0])
print(dev[1])
print(dev[4])
print(dev[10])

#task 5
negative = "Programming"
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-11])

#task 6
name = "Sanjeev Kumar"
print(name[0])
print(name[-1])
print(name[8])

#part 5
#task 7
slicing = "Python Programming"
print(slicing[0:6])
print(slicing[7:18])
print(slicing[0:18])
print(slicing[:5])
print(slicing[13:18])

#task 8
alphabet = "ABCDEFGHIJKL"
print(alphabet[::2])
print(alphabet[::3])
print(alphabet[1:8:2])
print(alphabet[::-1])

#task 9
text = "Python Programming"
print(text[-5:])
print(text[-10:])
print(text[::-1])

#task 10
city = "queenstown"
print(city[0:3])
print(city[-3:])
print(city[::2])
print(city[::-1])
print(city[1:9])

#part 6
#task 11
word = "Hello"
sentence = "Observehowspacesaffecttheresult"
sentence_with_spaces = "Observe how spaces affect the result"
print(len(word))
print(len(sentence))
print(len(sentence_with_spaces))

#task 12
text = "Python Programming"
print(len(text)-1)

#part 7
#task 13
first_name = "Sanjeev"
last_name = "Kumar"
print(first_name + " " + last_name)

#task 14
name = "Sanjeev"
age = 25
city = "Patna"
programming_language = "Python"
print("my name is " + name + " and I am " + str(age) + " years old" + " and I live in " + city + " and my favorite programming language is " + programming_language + ".")

#task 15
name = "Sanjeev"
age = 25
print(name + str(age) )

#task 16
word = "Python"
print(word * 3)
text = "Hello"
print(text * 5)
name = "Sanjeev"
print(name * 10)

#task 17
stars = "*"
print(stars * 10)

#task 18
case="python programming language"
print(case.upper())
print(case.lower())
print(case.capitalize())
print(case.title())
print(case.swapcase())

#task 19
capital="Python"
lower="python"
print(capital==lower)

#task 20
a="Python is a programming language"
print("Python" in a)
print("programming" in a)
print("language" in a)
print("Java" in a)

#task 21
b="Python is a programming language"
print(b.find("Python"))
print(b.find("programming"))
print(b.find("language"))
print(b.find("Java"))

#task 22
c="Python is a programming language"
print(c.index("Python"))
print(c.index("programming"))
print(c.index("language"))

#task 23
d="banana"
print(d.count("banana"))
print(d.count("a"))
print(d.count("b"))
print(d.count("n"))

#task 24
filename = "student_notes.pdf"
print(filename.endswith(".pdf"))
print(filename.startswith("student"))
print(filename.find(".txt"))

#task 25
text = "I am learning Java"
print(text.replace("Java", "Python"))

#task 26
text = "apple apple apple"
print(text.replace("apple", "mango"))

#task 27
text = "apple aapple apple"
print(text.replace("apple", "mango", 1))

#task 28
text = "Python"
text = text.upper()
print(text)

#task 29
text = "   Python Programming   "
print(text.strip())

#task 30
