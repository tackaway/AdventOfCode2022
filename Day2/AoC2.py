score=0
f = open("input.txt", "r")   #Open the file
for x in f: 
    if(x.replace(" ", "")[0] == "A"):     #If the first value is A (Rock)
        if(x.replace(" ", "")[1] == "X"): #X (Rock) is tied with A (Rock) = 1 + 3
            score+=4
        if(x.replace(" ", "")[1] == "Y"): #Y (Paper) beats A (Rock) = 1 + 6
            score+=8
        if(x.replace(" ", "")[1] == "Z"): #Z (Scissors) loses to A (Rock) = 1 + 0
            score+=3
    if(x.replace(" ", "")[0] == "B"):     #If the first value is B (Paper)
        if(x.replace(" ", "")[1] == "X"): #X (Rock) loses to B (Paper) = 1 + 0
            score+=1
        if(x.replace(" ", "")[1] == "Y"): #Y (Paper) ties to B (Paper) = 2 + 3
            score+=5
        if(x.replace(" ", "")[1] == "Z"): #Z (Scissors) win against B (Paper) = 3 + 6
            score+=9
    if(x.replace(" ", "")[0] == "C"):     #If the first value is C (Scissors)
        if(x.replace(" ", "")[1] == "X"): #X (Rock) wins against C (Scissors) = 1 + 6
            score+=7
        if(x.replace(" ", "")[1] == "Y"): #Y (Paper) loses to C (Scissors) = 2 + 0
            score+=2
        if(x.replace(" ", "")[1] == "Z"): #Z (Scissors) ties to C (Scissors) = 3 + 3
            score+=6
print(score)


