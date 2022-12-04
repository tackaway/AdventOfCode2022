count=0
f = open("input.txt", "r")   #Open the file
for x in f:
    r1s = int(x.partition(",")[0].partition("-")[0].strip())        #Get the first set starting value
    r1e = int(x.partition(",")[0].partition("-")[2].strip())        #Get the first set ending value
    r2s = int(x.partition(",")[2].partition("-")[0].strip())        #Get the second set starting value
    r2e = int(x.partition(",")[2].partition("-")[2].strip())        #Get the second set ending value
    
    if ((r1s in range(r2s,r2e+1) or r2s in range(r1s,r1e+1))):      #Check to see if any value is in the range
        count+=1                                                    #Increment
print(count)                                                        #Print Results