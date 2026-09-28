#Q5
sen=input("Enter a Sentence:")
words=sen.split()
short=0
medium=0
long=0

for w in words:
    if len(w)<=3:
        short+=1
        print("Short",len(w))
    elif 4<=len(w)<=6:
        medium+=1
        print("Medium",len(w))
    elif len(w)>6:
        long+=1
        print("Long",len(w))

print("Short Word Count:",short)
print("Medium Word Count:",medium)
print("Long Word Count:",long)


                   


