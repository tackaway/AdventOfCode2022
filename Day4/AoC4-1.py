count=0
f = open("input.txt", "r")   #Open the file
for x in f:
    r1s = int(x.partition(",")[0].partition("-")[0].strip())        #Get the first set starting value
    r1e = int(x.partition(",")[0].partition("-")[2].strip())        #Get the first set ending value
    r2s = int(x.partition(",")[2].partition("-")[0].strip())        #Get the second set starting value
    r2e = int(x.partition(",")[2].partition("-")[2].strip())        #Get the second set ending value
    if((r2s >= r1s and r2e <= r1e) or (r1s >= r2s and r1e <= r2e)): #Check to see if one set is fully inside another
        count+=1                                                    #Increment
print(count)                                                        #Print the final value


