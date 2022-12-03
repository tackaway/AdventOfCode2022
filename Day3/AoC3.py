##############################################################
#Function to discover the matching string in each rucksack
#
#Takes inputs A and B (first compartment, second compartment)
##############################################################
def diff(a,b):
    new_a, new_b, x = [a[x] for x in range(len(a))],[b[x] for x in range(len(b))],""
    for y in new_a:       #for each value in first compartment
        if(y in new_b):   #check to see if its in the second compartment
            x=y
    return x              #return that value

asciiVal,total=0,0
f = open("input.txt", "r")   #Open the file
for x in f:
    newx = x.strip()         #Remove newline characters
    asciiVal = ord(diff(newx[0:int(len(newx)/2)], newx[int(len(newx)/2):])) #retrive the ascii value
    if(asciiVal>90):         #Check for lowercase
        total+= asciiVal-96  #subtract for the difference
    else:                    #Check for uppercase
        total+= asciiVal- 38 #subtract for the difference
print(total)                 #return the final answer
