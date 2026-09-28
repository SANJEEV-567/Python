#Q3
sentence = input("Enter a sentence: ")
words = sentence.split()

highest_word = ""
highest_score=0

for w in words:
    score=0
    for char in w:
        if char in 'aeiouAEIOU':
            score+=2
        elif "a"<=char<="z" or "A"<=char<="Z":
            score+=1
        elif  "0"<=char<="9":
            score+=3
        else:
            score+=4
    print(f"Word:{w} with Score:{score}") 
    if score > highest_score:
        highest_score =score
        highest_word=w
print(f"Highest Scoring Word: '{highest_word}' with score {highest_score}")
       

        


