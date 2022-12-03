##############################################################
#Function to discover the matching string in each rucksack
#
#Takes inputs A, B, and C (first bag, second bag, third bag)
##############################################################
def diff(a,b,c):
    new_a, new_b, new_c, x = [a[x] for x in range(len(a))],[b[x] for x in range(len(b))],[c[x] for x in range(len(c))],""
    for y in new_a:             #for each value in first bag
        if(y in new_b):         #check to see if its in the second bag
            if(y in new_c):     #check to see if its in the third bag
                x=y
    return x              #return that value

asciiVal,total=0,0
f = open("input.txt", "r")   #Open the file
newx=[]
for x in f:
    newx.append(x.strip())         #Remove newline characters and append to array
for x in range(0,len(newx),3):     #From the array, loop incrementing every 3
    asciiVal=(ord(diff(newx[x],newx[x+1],newx[x+2])))#Take the 3 consecutive bags, and pass to diff, return ascii
    if(asciiVal>90):         #Check for lowercase
        total+= asciiVal-96  #subtract for the difference
    else:                    #Check for uppercase
        total+= asciiVal- 38 #subtract for the difference
print(total)                 #return the final answer
