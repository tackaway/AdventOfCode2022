elf, y, pos, val= 0,0,0,0    #Define Variables and Array
elfs = []
f = open("input.txt", "r")   #Open the file
for x in f:                  #Iterate through each line
    if(x=="\n"):             #Check for blank line
        elfs.append(elf)     #Add total calories to elf array
        elf=0                #Reset elf counter
    else:
        elf+=int(x)          #Add each elf calories 
print("Value of highest Elf: " + str(max(elfs)))                 #Find max of Elfs
print("Position of highest Elf: " + str(elfs.index(max(elfs))))  #Find position of Elfs
elfs = sorted(elfs, reverse=True)     #Sort array
print("The top 3 elfs are carrying " + str(elfs[0]+elfs[1]+elfs[2]) + " calories") #Print top 3 array results 