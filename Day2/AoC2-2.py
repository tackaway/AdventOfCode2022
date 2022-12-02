score=0
f = open("input.txt", "r")   #Open the file
for x in f: 
    if(x.replace(" ", "")[1] == "X"):     #If the last value is X (Lose)
        if(x.replace(" ", "")[0] == "A"): #Lose to A (Rock) is Z (Scissors) = 3 + 0
            score+=3
        if(x.replace(" ", "")[0] == "B"): #Lose to B (Paper) is X (Rock) = 1 + 0
            score+=1
        if(x.replace(" ", "")[0] == "C"): #Lose to C (Scissors) is Y (Paper) = 2 + 0
            score+=2
    if(x.replace(" ", "")[1] == "Y"):     #If the last value is Y (Draw)
        if(x.replace(" ", "")[0] == "A"): #Tie to A (Rock) is X (Rock) = 1 + 3
            score+=4
        if(x.replace(" ", "")[0] == "B"): #Tie to B (Paper) is Y (Paper) = 2 + 3
            score+=5
        if(x.replace(" ", "")[0] == "C"): #Tie to C (Scissors) is Z (Scissors) = 3 + 3
            score+=6
    if(x.replace(" ", "")[1] == "Z"):     #If the last value is Z (Win)
        if(x.replace(" ", "")[0] == "A"): #Win to A (Rock) is Y (Paper) = 2 + 6
            score+=8
        if(x.replace(" ", "")[0] == "B"): #Win to B (Paper) is Z (Scissors) = 3 + 6
            score+=9
        if(x.replace(" ", "")[0] == "C"): #Win to C (Scissors) is X (Rock) = 1 + 6
            score+=7
print(score)

