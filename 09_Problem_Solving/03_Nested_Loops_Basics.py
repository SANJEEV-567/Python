#Q11
for i in range(6):
    a=64
    for j in range(i):
        a+=1
        print(chr(a),end=" ")
    print()    

#Q12
a=64
for i in range(1,6):
    a+=1
    for j in range(i):
        print(chr(a),end=" ")
    print()

#Q13
for i in range(1, 10, 2):
    for j in range(1, i + 1, 2):
        print(j, end=" ")
    print() 

#Q14
for i in range(2, 11, 2):
    for j in range(2, i + 1, 2):
        print(j, end=" ")
    print()  

#Q15
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()  

#Q16
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()       

#Q17
a=0
for i in range(3):
    for j in range(3):
        a+=1
        print(a,end=" ")
    print()    

#Q18
a=0
for i in range(4):
    for j in range(5):
        a+=1
        print(a,end=" ")
    print()  

#Q19
for i in range(1,4):
    for j in range(1,4):
        print((i,j),end="") 
    print()

#Q20
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
#Q21
for i in range(1,11):
    for j in range(1,11):        
        print(i*j,end=" ")
    print()    

#Q22
for i in range(6):
    for j in range(i):
        print(i,end=" ")
    print()        

#Q23
for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end="")
    print()    

#Q24
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j, end="")
    print()    

#Q25
for i in range(1,6):
    for j in range(5):
        print(i,end="")
    print()          

#Q5
for i in range(1,5):
    for j in range(4,i-1,-1):
        print("*",end="")
    print() 
#Q6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()   

#Q7
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

#Q8
for i in range(1,6):
    for j in range(1,11):
        print(i*j,end=" ")
    print()  

#Q9

for i in range(1,4):
    for j in range(1,6):
        print(i*j,end=" ")
    print()   

#Q10
for i in range(1,6):
    for j in range(1,6):
        print(j**2,end=" ")
    print()     

#Q11
for i in range(1,6):
    a=64
    for j in range(i):
        a+=1
        print(chr(a),end=" ")
    print()           

#Q12
a=64
for i in range(1,6):
    a+=1
    for j in range(i):
        print(chr(a),end=" ")
    print()  

#Q13
for i in range(1,10,2):
    for j in range(1,i+1,2):
        print(j,end="")   
    print()    

#Q14
for i in range(2,11,2):
    for j in range(2,i+1,2):
        print(j,end=" ")
    print() 

#Q15
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print() 

#Q16    
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()  

#Q17
a=0
for i in range(3):
    for j in range(3):
        a+=1 
        print(a,end=" ")
    print()  

#Q18
a=0
for i in range(5):
    for j in range(5):
        a+=1
        print(a,end=" ")
    print()  

#Q19
for i in range(1,4):
    for j in range(1,4):
        print((i,j),end=" ")
    print()  

#Q20
for i in range(1,4):
    for j in range(1,4):
        print(i,j) 

#Q13 M-2
n=int(input("Enter No of Rows:"))
for i in range(n+1):
    for j in range(2*i+1):
        if j%2!=0:
            print(j,end=" ")
    print()        

#Q14 M-2
n=int(input("Enter No of Rows:"))
for i in range(1,n+1):
    for j in range(1,2*i):
        if j%2==0:
            print(j,end=" ")
    print()        
                
    



